# Virtual-Memory-Management-Simulator
The memory management simulator is used to simulate page fault behavior in a paged virtual memory system. The program employs a few replacement algorithms and traces a set of instructions which are specified in the command line.

# Running the Simulator
optional arguments:
  -h, --help  show this help message and exit
  
   -ps PS      page size 
   
  -tp TP      total_number_of_page_frames (in main memory)
  
  -r R        number_of_page_frames_per_process for FIFO, LRU, LRU-K, LFU and OPT, or delta (window size) for the Working Set algorithm
  
  -x X        lookahead window size for OPT, X for LRU-X, 0 for others (which do not use this value)
  
  -min MIN    min free pool size
  
  -max MAX    max free pool size
  
  -k K        total number of processes
  
  
 # Example.

python3 simulator.py -ps 4 -tp "7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2"  -r 3 -x 5 -min 4 -max 7 -k 6

 # Warning.
If you run without the arguments. it will result in errors
