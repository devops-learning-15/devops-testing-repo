from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from server_utilities import *

class handler(BaseHTTPRequestHandler):

	changed_path = ""

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		print("\n\n", self.path, "\n\n")

		if self.path[1:] == '':
			self.wfile.write(bytes(question_page(),'utf-8'))

		elif "?" in self.path[1:]:
			z = self.path[1:].split("?")
			self.changed_path = z[1]

			if "nth_prime" in self.changed_path:
				b = self.changed_path.replace('nth_prime', '').replace('=','')
				if b.isnumeric():
					lst = prime(int(b))
					self.wfile.write(bytes(str(making_list("The nth prime numbers are : ",lst)),'utf-8'))
					self.changed_path = ""
				else:
					self.wfile.write(bytes(error_page(), 'utf-8'))

			elif "sum_of_squares" in self.changed_path:
				self.condition_operators('sum_of_squares', "The nth sum of squares of", recursive_sum_of_square)
				
			elif "sum_of_factorial" in self.changed_path:
				self.condition_operators('sum_of_factorial', "The sum of nth factorial of", sum_of_factorial_recursive)

			elif "sum_of_cubes" in self.changed_path:
				self.condition_operators('sum_of_cubes', "The nth sum of cubes of", recursive_sum_of_cube)

			elif "prime" in self.changed_path:
				self.condition_operators('prime', "It is a Prime Number ???", is_prime)

			elif "nth_sum" in self.changed_path:
				self.condition_operators('nth_sum', "The nth sum of", recursive_sum)

			elif "square" in self.changed_path:
				self.condition_operators('square', "The square of", squares)

			elif "cube" in self.changed_path:
				self.condition_operators('cube', "The cube of", cubes)

			elif "factorial" in self.changed_path:
				self.condition_operators('factorial', "The factorial of", factorial_recursive)

			else:
				self.wfile.write(bytes(error_page(), 'utf-8'))

		else:
			self.wfile.write(bytes(error_page(), 'utf-8'))


	def condition_operators(self, replace_statement, statement, func):
		num = self.changed_path.replace(replace_statement, '').replace('=','')
		if num.isnumeric():
			self.wfile.write(bytes(one_line_answer(statement+' '+num+" =", func(int(num))), 'utf-8'))
			self.changed_path = ""
		else:
			self.wfile.write(bytes(error_page(), 'utf-8'))


try:
	with HTTPServer(('localhost', 4444), handler) as server:
		server.serve_forever()
except KeyboardInterrupt:
	pass