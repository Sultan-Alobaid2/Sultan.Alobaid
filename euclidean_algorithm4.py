{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;\f2\froman\fcharset0 TimesNewRomanPSMT;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa160\partightenfactor0

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class EuclideanAlgorithm:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0Class to encapsulate the Euclidean Algorithm.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0"""
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa160\partightenfactor0

\f0\fs32 \cf0 \'a0\'a0\'a0\'a0def gcd(self, a, b):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Compute the greatest common divisor (GCD) of two positive integers.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param a: First positive integer.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param b: Second positive integer.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:return: GCD of a and b.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
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

\f0\fs32 class EuclideanAlgorithm:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0Class to encapsulate the Euclidean Algorithm.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0"""
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa160\partightenfactor0

\f0\fs32 \cf0 \'a0\'a0\'a0\'a0def gcd(self, a, b):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Compute the greatest common divisor (GCD) of two positive integers.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param a: First positive integer.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:param b: Second positive integer.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:return: GCD of a and b.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
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
\pard\pardeftab720\sa160\partightenfactor0

\f0\fs32 \cf0 \'a0\'a0\'a0\'a0def get_input(self):
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Get validated user input.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:return: Two positive integers.
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while True:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0try:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = int(input("Enter the first positive integer: "))
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = int(input("Enter the second positive integer: "))
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0if a > 0 and b > 0:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a, b
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0else:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0print("Both numbers must be positive integers. Please try again.")
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0except ValueError:
\f1\fs24 \

\f0\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0print("Invalid input. Please enter positive integers only.")
\f1\fs24 \
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f2\fs32 \cf0 \strokec2 class EuclideanAlgorithm:
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0def gcd(self, a, b):
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while b != 0:
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0temp = b
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = a % b
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = temp
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \strokec2 \
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f2\fs32 \cf0 \strokec2 \'a0\'a0\'a0\'a0def lcm(self, a, b):
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return (a * b) // self.gcd(a, b)
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \strokec2 \
\pard\pardeftab720\li960\fi-960\sa373\partightenfactor0

\f2\fs32 \cf0 \strokec2 if __name__ == "__main__":
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0algo = EuclideanAlgorithm()
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0a, b = algo.get_input()
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0print(f"GCD of \{a\} and \{b\} is: \{algo.gcd(a, b)\}")
\f1\fs24 \

\f2\fs32 \'a0\'a0\'a0\'a0print(f"LCM of \{a\} and \{b\} is: \{algo.lcm(a, b)\}")
\f1\fs24 \
}