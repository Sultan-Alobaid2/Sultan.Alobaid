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
class EuclideanAlgorithm:\
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
\
\'a0\'a0\'a0\'a0def get_input(self):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0Get validated user input.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0:return: Two positive integers.\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0"""\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while True:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0try:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = int(input("Enter the first positive integer: "))\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = int(input("Enter the second positive integer: "))\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0if a > 0 and b > 0:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a, b\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0else:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0print("Both numbers must be positive integers. Please try again.")\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0except ValueError:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0print("Invalid input. Please enter positive integers only.")\
class EuclideanAlgorithm:\
\'a0\'a0\'a0\'a0def gcd(self, a, b):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0while b != 0:\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0temp = b\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0b = a % b\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0a = temp\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return a\
\
\'a0\'a0\'a0\'a0def lcm(self, a, b):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0return (a * b) // self.gcd(a, b)\
\
if __name__ == "__main__":\
\'a0\'a0\'a0\'a0algo = EuclideanAlgorithm()\
\'a0\'a0\'a0\'a0a, b = algo.get_input()\
\'a0\'a0\'a0\'a0print(f"GCD of \{a\} and \{b\} is: \{algo.gcd(a, b)\}")\
\pard\pardeftab560\li880\slleading20\partightenfactor0
\cf0 \'a0\'a0\'a0\'a0print(f"LCM of \{a\} and \{b\} is: \{algo.lcm(a, b)\}")\
}