#!/usr/bin/perl -w 

use Encode;
use utf8;
use CGI;
use Switch;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

$form = new CGI;

#for interface language
$langdesgn = $ARGV[0];
my $btnDownload="";

if ($langdesgn eq "az") {
	$btnDownload="mp3&nbsp;kimi&nbsp;y&uuml;kl&#601;";
}
else {
	$btnDownload="&nbsp;Download as mp3";
}

################################# Sample functions #############################
sub rtrim($)
{
	my $string = shift;
	$string =~ s/\s+$//;
	return $string;
}

sub ltrim
{
	my $string=shift;
	$string=~ s/^\s+//;
	return $string;
}

my $text_self;
my $object_tts;
my $mp3_link;

$remotehost = $form->remote_host();

my @suggest_from = $form->param('from');

$text_self = decode("utf-8", @suggest_from[0]);

$tts_text = $text_self;


#flashplayerin oldughu papka
$home_dir = "../../";

$tmpdir = "../../temp";
$tmpdir2 = "../../temp";
$exectext2wave = "../../tts -fa %s";

$tts_text = lc($tts_text);
%tr=(
"ə" => "ee", "ü" => "uu", "ö" => "oo", "ş" => "sh", "ç" => "ch", "ğ" => "gh", "ı" => "ii", "İ" => "ii", "ё" => "yo", "й" => "y", "ц" => "s", "у" => "u", "к" => "k", "е" => "e", "н" => "n", "г" => "q", "ш" => "ş", "щ" => "ş", "з" => "z", "х" => "x", "ъ" => "", "ф" => "f", "ы" => "ı", "в" => "v", "а" => "a", "п" => "p", "р" => "r", "о" => "o", "л" => "l", "д" => "d", "ж" => "j", "э" => "e", "я" => "ya", "ч" => "ç", "с" => "s", "м" => "m", "и" => "i", "т" => "t", "ь" => "", "б" => "b", "ю" => "yu"
);
$tts_text =~ s/(ə|ü|ö|ş|ç|ğ|ı|İ|ё|й|ц|у|к|е|н|г|ш|щ|з|х|ъ|ф|ы|в|а|п|р|о|л|д|ж|э|я|ч|с|м|и|т|ь|б|ю)/$tr{$1}/g;

if ($tts_text ne "") {
  #get current date
  my ($sec,$min,$hour,$day,$month,$yr19,@rest) =  localtime(time);
  $filename = $day.++$month.($yr19+1900).sprintf("%02d",$hour).sprintf("%02d",$min).sprintf("%02d",$sec);

  $from_file = $tmpdir."/".$filename.".txt";
  
  $wave_file = $tmpdir."/".$filename.".wav";
  $wave_file2 = $tmpdir2."/".$filename.".wav";
  $mp3_file  = $tmpdir."/".$filename.".mp3";
  $mp3_file2  = $tmpdir2."/".$filename.".mp3";
  $mp3_file_download = $filename.".mp3";

  #open the temp file for writing
  open my $FH, ">:utf8", $from_file;
  print $FH $tts_text;
  close $FH;

  #open the log file for writing
  open my $FH, ">>:utf8", "../../temp/logtts.log";
  print $FH $remotehost."--->".$text_self."\n\n";
  close $FH;
  
  #if the from file exists, use tts
  if (-e $from_file) {
	$text2wave_cmd = sprintf($exectext2wave,$from_file);
	#print $text2wave_cmd."<br>";
	#`touch tmp/ramin.txt`;
	#`touch ../../temp/ramil.txt`;
	`$text2wave_cmd`;

	$save_mp3 = 1;
	#print "<br>a=".$lame_cmd;
	#create an mp3 version?
	if ($save_mp3) {
		$lame_cmd = sprintf("lame %s %s",$wave_file,$mp3_file);			
		`$lame_cmd`;
		#delete the WAV, TRACE, LAB file to conserve space
		unlink($wave_file);
		$wave_file =~ s/\.wav/\.trace/gi; 
		unlink($wave_file);
		$wave_file =~ s/\.trace/\.lab/gi; 
		unlink($wave_file);
	}

	#delete the temp from file
	#unlink($from_file);
  }
}

=c
   $object_tts = '<script type="text/javascript" src="'.$home_dir.'/audio_player/audio-player.js"></script>  
    <script type="text/javascript">  
        AudioPlayer.setup("'.$home_dir.'/audio_player/player.swf", {  
            width: 290  
        });  
    </script>  

    <script type="text/javascript">  
    AudioPlayer.embed("audioplayer_1", {soundFile: "'.$mp3_file2.'",  autostart: "yes",  animation: "no",  titles: " ", lefticon: "cccccc", righticon: "4b8bc2", rightbg: "cccccc"});  
    </script>';
=cut

$object_tts = '<object type="application/x-shockwave-flash" data="'.$home_dir.'/audio_player/player_mp3_maxi.swf" width="250" height="24">
	<param name="wmode" value="transparent" />
	<param name="movie" value="'.$home_dir.'/audio_player/player_mp3_maxi.swf" />
	<param name="FlashVars" value="mp3='.$mp3_file2.'&bgcolor1=cccccc&showstop=1&bgcolor2=cccccc&buttoncolor=4a8ac1&buttonovercolor=0&slidercolor1=4a8ac1&slidercolor2=4a8ac1&sliderovercolor=666666&textcolor=0&showvolume=1&autoplay=1" />
</object>';

$mp3_link = "<form action=\"../../download.php?filename=$mp3_file_download\" method=\"POST\" target=\"_self\"><input type=\"button\" name=\"make_audio_mp\" class=\"dlc_button_mp3\" value=\"&nbsp;&nbsp;&nbsp;$btnDownload\" id=\"make_audio_mp_id\" onclick=\"Javascript:window.open('../../download.php?filename=$mp3_file_download');\"></form>";

print $form->header;
print $mp3_link;
print $object_tts;

#print $mp3_link.$object_tts;
#print "<p> Your  IP  is: <b>$remotehost</b></p>";
