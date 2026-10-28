class ansi:
	string: str
	attributes: list[str]
	
	def __init__(self, string: str):
		self.string = str(string)
		self.attributes = []
		
		
	def __repr__(self) -> str:
		output = ""
		
		match len(self.attributes):
			case 0:
				output += "0"
				
			case 1:
				output += self.attributes[0]
				
			case attr_len:
				i: int = 0
				while i < attr_len - 1:
					output += self.attributes[i] + ';'
					i += 1
					
				output += self.attributes[-1]
				
				
		return f"\033[{output}m{self.string}\033[0m"
		
		
	def none(self) -> ansi:				self.attributes.append("0"); return self
	def bold(self) -> ansi:				self.attributes.append("1"); return self
	def dim(self) -> ansi:				self.attributes.append("2"); return self
	def italic(self) -> ansi:			self.attributes.append("3"); return self
	def underline(self) -> ansi:		self.attributes.append("4"); return self
	def blink(self) -> ansi:			self.attributes.append("5"); return self
	def reverse(self) -> ansi:			self.attributes.append("7"); return self
	def hide(self) -> ansi:				self.attributes.append("8"); return self
	def strikethrough(self) -> ansi:	self.attributes.append("9"); return self
	
	def black(self) -> ansi:			self.attributes.append("30"); return self
	def red(self) -> ansi:				self.attributes.append("31"); return self
	def green(self) -> ansi:			self.attributes.append("32"); return self
	def yellow(self) -> ansi:			self.attributes.append("33"); return self
	def blue(self) -> ansi:				self.attributes.append("34"); return self
	def magenta(self) -> ansi:			self.attributes.append("35"); return self
	def cyan(self) -> ansi:				self.attributes.append("36"); return self
	def white(self) -> ansi:			self.attributes.append("37"); return self
	
	def bg_black(self) -> ansi:			self.attributes.append("40"); return self
	def bg_red(self) -> ansi:			self.attributes.append("41"); return self
	def bg_green(self) -> ansi:			self.attributes.append("42"); return self
	def bg_yellow(self) -> ansi:		self.attributes.append("43"); return self
	def bg_blue(self) -> ansi:			self.attributes.append("44"); return self
	def bg_magenta(self) -> ansi:		self.attributes.append("45"); return self
	def bg_cyan(self) -> ansi:			self.attributes.append("46"); return self
	def bg_white(self) -> ansi:			self.attributes.append("47"); return self
	
	def bright_black(self) -> ansi:		self.attributes.append("90"); return self
	def bright_red(self) -> ansi:		self.attributes.append("91"); return self
	def bright_green(self) -> ansi:		self.attributes.append("92"); return self
	def bright_yellow(self) -> ansi:	self.attributes.append("93"); return self
	def bright_blue(self) -> ansi:		self.attributes.append("94"); return self
	def bright_magenta(self) -> ansi:	self.attributes.append("95"); return self
	def bright_cyan(self) -> ansi:		self.attributes.append("96"); return self
	def bright_white(self) -> ansi:		self.attributes.append("97"); return self
