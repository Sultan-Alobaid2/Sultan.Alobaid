{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class EuclideanAlgorithm:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0def gcd(self, a, b):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while b != 0:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0temp = b
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = a % b
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = temp
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f0\fs32 \cf0 \'a0\'a0\'a0\'a0def lcm(self, a, b):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return (a * b) // self.gcd(a, b)
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f0\fs32 \cf0 if __name__ == "__main__":
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0algo = EuclideanAlgorithm()
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0a, b = algo.get_input()
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0print(f"GCD of \{a\} and \{b\} is: \{algo.gcd(a, b)\}")
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0print(f"LCM of \{a\} and \{b\} is: \{algo.lcm(a, b)\}")
\f1\fs24 \
}