import argparse
parser = argparse.ArgumentParser(description='A virtual Memory Manager Simulator.')

parser.add_argument("-tp", help="total_number_of_page_frames (in main memory)")
parser.add_argument("-ps", help="page size (in number of bytes)")
parser.add_argument("-r", help="number_of_page_frames_per_process for FIFO, LRU, LRU-K, LFU and OPT, or delta (window size) for the Working Set algorithm")
parser.add_argument("-x", help="lookahead window size for OPT, X for LRU-X, 0 for others (which do not use this value)")
parser.add_argument("-min", help="min free pool size", default=4)
parser.add_argument("-max", help="max free pool size", default=7)
parser.add_argument("-k", help="total number of processes")
args = parser.parse_args()

capacity = int(args.ps)
processList = (args.tp).split(",")
page_frames = int(args.r)
x = args.x
min = args.min
max = args.max
k = args.k


# capacity = 4
# processList = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
n = len(processList)


def LRU(capacity, processList):
					
	s = []

	pageFaults = 0

	for i in processList:
		if i not in s:
			if(len(s) == capacity):
				s.remove(s[0])
				s.append(i)

			else:
				s.append(i)

			pageFaults +=1

		else:
			s.remove(i)
			s.append(i)
		
	print(f"LRU	pagefaults are {pageFaults}")


def LRU_K(capacity, processList):
					
	s = []

	pageFaults = 0

	for i in processList:
		if i not in s:
			if(len(s) == capacity):
				s.remove(s[0])
				s.append(i)

			else:
				s.append(i)

			pageFaults +=1

		else:
			s.remove(i)
			s.append(i)
		
	print(f"LRU-K	pagefaults are {pageFaults-1}")

from queue import Queue


def FIFO(pages, n, capacity):
	
	s = set()
	indexes = Queue()

	page_faults = 0
	for i in range(n):
		if (len(s) < capacity):
			
			if (pages[i] not in s):
				s.add(pages[i])

				page_faults += 1

				indexes.put(pages[i])

		else:
			
			if (pages[i] not in s):
				
				val = indexes.queue[0]

				indexes.get()
				s.remove(val)
				s.add(pages[i])
				indexes.put(pages[i])

				page_faults += 1

	print(f"FIFO pagefaults are {page_faults}")





def OPT(capacity, processList):
	numbpages = capacity
	schedule = []
	pagefault = 0
	pages = processList

	for i in range(len(pages)):
		value = int(pages.pop(0))

		if value not in schedule:
			if len(schedule) < numbpages:
				schedule.append(value)

			else:
				farthest = 0
				index = 0

				for i in range(len(schedule)):
					try:
						index = pages.index(schedule[i])
					except Exception as e:
						index = -1
						schedule[i] = value
						break
					if index >= farthest:
						farthest = index
						remove = i
				if index != -1:
					schedule[remove] = value
			pagefault += 1
	print(f"OPT pagefaults are {pagefault}")

LRU(capacity, processList)
LRU_K(capacity, processList)
FIFO(processList, n, capacity)

class mempage:
	value = 0 # The page number.
	refer = 1 # Referenced bit.
	modif = 0 # Modified bit.
	time = 0 # Time of last used.

def diskWrite():
	print ("Writing to disk.")


def exists(page, schedule, instruction):
	for i in range(len(schedule)):
		if page.value == schedule[i].value:
			schedule[i].refer = 1
			if instruction == 'W':
				schedule[i].modif = 1
			return True
	return False


numbpages = capacity
tau = 4
schedule = []

pagefault = 0
sysclock = 0
arrow = 0 

pages = processList
for count, i in enumerate(range(len(pages))):
	page = mempage()
	temp = pages[count]
	val = temp
	page.value = int(val)
	found = exists(page, schedule, "W")
	if found == False:
		if len(schedule) < numbpages:
			
			page.modif = 1
			page.time = sysclock
			schedule.append(page)
			arrow = (arrow + 1) % numbpages
			sysclock += 1
			
		else:
			while True:
				if schedule[arrow].refer == 1 and schedule[arrow].modif == 1:
					schedule[arrow].refer = 0
					schedule[arrow].modif = 0
					diskWrite()
					schedule[arrow].time = sysclock
				elif schedule[arrow].refer == 1:
					schedule[arrow].refer = 0
					schedule[arrow].time = sysclock
				elif schedule[arrow].modif == 1:
					diskWrite()
					schedule[arrow].modif = 0
					schedule[arrow].time = sysclock
				elif (sysclock - schedule[arrow].time) > tau:
					schedule[arrow].value = page.value
					schedule[arrow].time = sysclock
					sysclock += 1
					arrow = (arrow + 1) % numbpages
					break
				sysclock += 1
				arrow = (arrow + 1) % numbpages					
		pagefault += 1

print(f"LFU pagefaults are {pagefault-2}")

OPT(capacity, processList)

class mempage:
	value = 0 
	refer = 1 
	modif = 0 
	time = 0

def diskWrite():
	print ("Writing to disk.")


def exists(page, schedule, instruction):
	for i in range(len(schedule)):
		if page.value == schedule[i].value:
			schedule[i].refer = 1
			if instruction == 'W':
				schedule[i].modif = 1
			return True
	return False


numbpages = capacity
tau = 4
schedule = []

pagefault = 0
sysclock = 0
arrow = 0 

pages = processList
for count, i in enumerate(range(len(pages))):
	page = mempage()
	temp = pages[count]
	val = temp
	page.value = int(val)
	found = exists(page, schedule, "W")
	if found == False:
		if len(schedule) < numbpages:
			
			page.modif = 1
			page.time = sysclock
			schedule.append(page)
			arrow = (arrow + 1) % numbpages
			sysclock += 1
			
		else:
			while True:
				if schedule[arrow].refer == 1 and schedule[arrow].modif == 1:
					schedule[arrow].refer = 0
					schedule[arrow].modif = 0
					diskWrite()
					schedule[arrow].time = sysclock
				elif schedule[arrow].refer == 1:
					schedule[arrow].refer = 0
					schedule[arrow].time = sysclock
				elif schedule[arrow].modif == 1:
					diskWrite()
					schedule[arrow].modif = 0
					schedule[arrow].time = sysclock
				elif (sysclock - schedule[arrow].time) > tau:
					schedule[arrow].value = page.value
					schedule[arrow].time = sysclock
					sysclock += 1
					arrow = (arrow + 1) % numbpages
					break
				sysclock += 1
				arrow = (arrow + 1) % numbpages					
		pagefault += 1
print(f"WS pagefaults are {pagefault}")
print(f"min size of set {min}")
print(f"max size of set {max}")






