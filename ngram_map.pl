#!/usr/bin/perl -w 

use encoding "utf8";
use strict;
use warnings;
binmode (STDIN, "utf8");

sub generate_ngrams
{
	my $str = $_[0];
	my $order = $_[1];
	my $match = "\\S+";
	for (my $i=1;$i<$order;$i++)
	{
		$match = "$match"."\\s+\\S+";	
	}
	$match = qr/$match/;
	while ($str =~ m/($match)/gi)
	{
		print "$1\t1\n";
		$str =~ s/^\S+\s+//gi;
	}
}

while (<STDIN>)
{
	for (my $i=1;$i<=6;$i++) 
	{
		generate_ngrams($_,$i);
	}
}
