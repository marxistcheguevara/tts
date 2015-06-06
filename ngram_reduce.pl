#! /usr/bin/perl -w


use encoding "utf8";
use strict;
use warnings;


 
 
my $word="";
my $current_word="";
my $count=0;
my $current_count=0;

while(<STDIN>)
{
   chomp;
   if ($_=~/(.*)\t(.*)/gi)
    {
	#$hash{$1}++;
	$word=$1;
	$count=$2;
        if ($current_word eq $word)
             {
                $current_count+=$count;
             }
        else {
            if( $current_word ne "")
              {
                 print "$current_word\t$current_count\n";
              }
              $current_word = $word;
              $current_count = $count;
             }
        
    }   
}
if ($current_word eq $word)
   {
        print "$current_word\t"."$current_count\n";
   }



