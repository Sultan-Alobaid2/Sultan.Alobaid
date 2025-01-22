{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\fs26 \cf0 class EuclideanAlgorithm:\
\'a0\'a0\'a0\'a0"""\
\'a0\'a0\'a0\'a0Class to encapsulate the Euclidean Algorithm.\
\'a0\'a0\'a0\'a0"""\
\
\'a0\'a0\'a0\'a0def gcd(self, a, b):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Compute the greatest common divisor (GCD) of two positive integers.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param a: First positive integer.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param b: Second positive integer.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:return: GCD of a and b.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while b != 0:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0temp = b\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = a % b\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = temp\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a\
}