class ansi:
	string: str
	attributes: list[str]
	
	def __init__(self, string: str):
		self.string = str(string)
		self.attributes = []
		
		
	def __repr__(self) -> str:
		output: str
		
		match len(self.attributes):
			case 0:
				output = "0"
				
			case 1:
				output = self.attributes[0]
				
			case attr_len:
				output = ""
				
				i: int = 0
				while i < attr_len - 1:
					output += self.attributes[i] + ';'
					i += 1
					
				output += self.attributes[-1]
				
				
		return f"\033[{output}m{self.string}\033[0m"
	
	
	# effects 0-5 and 7-9
	def none(self) -> ansi:				self.attributes.append("0"); return self
	def bold(self) -> ansi:				self.attributes.append("1"); return self
	def dim(self) -> ansi:				self.attributes.append("2"); return self
	def italic(self) -> ansi:			self.attributes.append("3"); return self
	def underline(self) -> ansi:		self.attributes.append("4"); return self
	def blink(self) -> ansi:			self.attributes.append("5"); return self
	def reverse(self) -> ansi:			self.attributes.append("7"); return self
	def hide(self) -> ansi:				self.attributes.append("8"); return self
	def strikethrough(self) -> ansi:	self.attributes.append("9"); return self
	
	# colours 30-37
	def black(self) -> ansi:			self.attributes.append("30"); return self
	def red(self) -> ansi:				self.attributes.append("31"); return self
	def green(self) -> ansi:			self.attributes.append("32"); return self
	def yellow(self) -> ansi:			self.attributes.append("33"); return self
	def blue(self) -> ansi:				self.attributes.append("34"); return self
	def magenta(self) -> ansi:			self.attributes.append("35"); return self
	def cyan(self) -> ansi:				self.attributes.append("36"); return self
	def white(self) -> ansi:			self.attributes.append("37"); return self
	
	# background colours 40-47
	def bg_black(self) -> ansi:			self.attributes.append("40"); return self
	def bg_red(self) -> ansi:			self.attributes.append("41"); return self
	def bg_green(self) -> ansi:			self.attributes.append("42"); return self
	def bg_yellow(self) -> ansi:		self.attributes.append("43"); return self
	def bg_blue(self) -> ansi:			self.attributes.append("44"); return self
	def bg_magenta(self) -> ansi:		self.attributes.append("45"); return self
	def bg_cyan(self) -> ansi:			self.attributes.append("46"); return self
	def bg_white(self) -> ansi:			self.attributes.append("47"); return self
	
	# bright colours 90-97
	def bright_black(self) -> ansi:		self.attributes.append("90"); return self
	def bright_red(self) -> ansi:		self.attributes.append("91"); return self
	def bright_green(self) -> ansi:		self.attributes.append("92"); return self
	def bright_yellow(self) -> ansi:	self.attributes.append("93"); return self
	def bright_blue(self) -> ansi:		self.attributes.append("94"); return self
	def bright_magenta(self) -> ansi:	self.attributes.append("95"); return self
	def bright_cyan(self) -> ansi:		self.attributes.append("96"); return self
	def bright_white(self) -> ansi:		self.attributes.append("97"); return self
	
	# 256-colour foreground
	def fg_256(self, n: int) -> ansi:
		assert(0 <= n <= 255)
		self.attributes.append("38")
		self.attributes.append("5")
		self.attributes.append(str(int(n)))
		return self
	
	# 256-colour background
	def bg_256(self, n: int) -> ansi:
		assert(0 <= n <= 255)
		self.attributes.append("48")
		self.attributes.append("5")
		self.attributes.append(str(int(n)))
		return self
	
	# 24-bit true colour foreground
	def fg_true_colour(self, r: int, g: int, b: int) -> ansi:
		assert(0 <= r <= 255)
		assert(0 <= g <= 255)
		assert(0 <= b <= 255)
		self.attributes.append("38")
		self.attributes.append("2")
		self.attributes.append(str(int(r)))
		self.attributes.append(str(int(g)))
		self.attributes.append(str(int(b)))
		return self
	
	# 24-bit true colour background
	def bg_true_colour(self, r: int, g: int, b: int) -> ansi:
		assert(0 <= r <= 255)
		assert(0 <= g <= 255)
		assert(0 <= b <= 255)
		self.attributes.append("48")
		self.attributes.append("2")
		self.attributes.append(str(int(r)))
		self.attributes.append(str(int(g)))
		self.attributes.append(str(int(b)))
		return self
	
	
	# aliases
	reset = none
	strike = strikethrough
	
	pink = magenta
	bg_pink = bg_magenta
	bright_pink = bright_magenta
	
	fg_24b = fg_true_colour
	bg_24b = bg_true_colour
