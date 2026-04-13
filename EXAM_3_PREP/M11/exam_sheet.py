'''
# LINEAR SEARCH O(n) — unsorted ok
def linearSearch(lst, target):
    for i in range(len(lst)):
        if lst[i] == target: return i
    return -1  # not found

# BINARY SEARCH O(log n) — MUST BE SORTED
def binarySearch(lst, target):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target: return mid
        elif lst[mid] < target: start = mid + 1
        else: end = mid - 1
    return -1


# KEY BEHAVIORS
# try/except stops at FIRST error — lines after error DON'T run
# projects["project 3"] → KeyError → jumps to except immediately
# print("project 1") NEVER runs

# catch specific errors in order:
except ZeroDivisionError as e:  # catches specific
except Exception as e:          # catches everything else

# AssertionError can be caught by except AssertionError as e:
# str(e) prints the assert message
assert num >= 0, "Cannot calculate square root of negative"
# → caught by except AssertionError as e: print(str(e))

# PURPOSE SUMMARY:
# assert = validate conditions (crashes if False)
# try/except = handle errors gracefully
# unittest = structured test cases with assertEqual etc



BIG O:
O(1)      — constant    — single line
O(log n)  — binary search, while i *= 2
O(n)      — linear search, single loop
O(n²)     — nested loops, all 3 sorts
consecutive loops → ADD → still O(n)
nested loops → MULTIPLY → O(n²)
ignore constants: O(5n) → O(n)
ignore lower terms: O(n²+3n) → O(n²)


git init          — start a repo
git clone <url>   — copy a repo
git add .         — stage changes
git commit -m ""  — save changes with message
git push          — upload to GitHub
git pull          — download updates
git status        — see what's changed
git log           — see commit history
'''

'''
try/except stops at FIRST error — lines after DON'T run
except catches in ORDER — first match wins
assert x > 0, "msg" → AssertionError if False
str(e) prints the assert/error message

self.x vs ClassName.x:
- self.x += 1 → creates INSTANCE var (shadows class)
- ClassName.x += 1 → modifies CLASS var
- instance.x = val → only affects THAT instance

andrea.increase_rate = 0.1 → only andrea changes
Employee.increase_rate = 0.03 → all instances without own var

class var list [] is MUTABLE → shared across ALL instances
class var int is NOT shared → self.x shadows it

instance method MUST have self
def method(): ← ERROR, def method(self): ← correct
super().__init__(x) ← no self / Parent.__init__(self, x) ← needs self

defaults must be TRAILING: f(x, y=1) ✓ f(x=1, y) ✗
Tree("Default") ← ERROR if type is required with no default

push = local→remote / pull = remote→local
commit = save locally / add = stage / clone = copy repo

Binary search iterations: [8,21,32,34,51,65] target=65
mid=34(idx2), 65>34 → right / mid=51(idx4), 65>51 → right / mid=65 found → 3 iterations

nested loops → O(n²) / consecutive → O(n) / i*=2 → O(log n)
'''

'''
DEBUGGING PATTERN:
line X: self.name = name (not name = self.name)
line X: def method(self): (missing self)
line X: use self.attr (not bare attr)
line X: obj.method() (missing parentheses)
line X: print(obj.name) (not obj.self.name)

PHONEBOOK PATTERN (dict with two lookups):
class PhoneBook:
    def __init__(self): self.contacts = {}
    def add_contact(self, name, number): self.contacts[name] = number
    def get_number(self, name): return self.contacts[name]
    def who_is(self, number):
        for name, num in self.contacts.items():
            if num == number: return name

INHERITANCE OVERRIDE PATTERN:
class Child(Parent):
    def __init__(self, a, b, extra):
        super().__init__(a, b)
        self.extra = extra
    def display_info(self):
        super().display_info()
        print(f"Extra: {self.extra}")
    def add_word(self, word):
        if word not in ["a", "an", "the"]:
            super().add_word(word)
    def print_counts(self):
        print("extra line first")
        super().print_counts()

DICT PATTERN:
def __init__(self): self.data = {}
if key not in self.data: self.data[key] = []
self.data[key].append(val)
for k, v in self.data.items(): print(k, v)
'''