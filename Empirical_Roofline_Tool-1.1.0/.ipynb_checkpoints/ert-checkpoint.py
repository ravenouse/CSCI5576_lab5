# Import builtin Python modules
import sys,os.path

# Import ERT python modules
from Python.ert_core  import ert_core
from Python.ert_utils import *

# Get the path to the directory where this was run
exe_path = os.path.dirname(sys.argv[0])
print(exe_path)
if exe_path == "":
  exe_path = "."

# Create the ERT object
ert = ert_core()

# Initialize the execution path
ert.exe_path = exe_path

# Parse the command line
if ert.flags() != 0:
  sys.stderr.write("\n--- Parsing command line arguments failed --- \n\n")
  sys.exit(1)
sys.stdout.flush()

# Configure the ERT using the configuration file given on the command line
if ert.configure() != 0:
  sys.stderr.write("\n--- Configuring ERT failed ---\n\n")
  sys.exit(1)
sys.stdout.flush()

# Get the list of flops/element to try (specified by the user)
flops_list = parse_int_list(ert.dict["CONFIG"]["ERT_FLOPS"][0])

# Go through the flops/element list and process each case
for flop in flops_list:
  # A bit of output if any verbosity has been requested
  if ert.options.verbose > 0:
    print("FLOP count %d..." % flop)
    sys.stdout.flush()

  # Set the ERT object flops/element
  ert.flop = flop

  # Create a directory for these experiments (and give it to the ERT object)
  ert.flop_dir = "%s/FLOPS.%03d" % (ert.results_dir,flop)
  make_dir_if_needed(ert.flop_dir,"run",ert.options.verbose > 1)

  # Build the current code with the current flops/element
  if ert.build() != 0:
    sys.stderr.write("\n--- Building ERT failed ---\n\n")
    sys.exit(1)
  sys.stdout.flush()

  # Run the built code over a variety of MPI, OpenMP, and/or CUDA
  # configurations specified by the user
  if ert.run() != 0:
    sys.stderr.write("\n--- Running ERT failed ---\n\n")
    sys.exit(1)
  sys.stdout.flush()

  # Process all the results for the current flops/element
  if ert.process() != 0:
    sys.stderr.write("\n--- Processing ERT results failed ---\n\n")
    sys.exit(1)
  sys.stdout.flush()

  # Make graphs of all the results for the current flops/element
  if ert.graphs() != 0:
    sys.stderr.write("\n--- Making ERT individual graphs failed ---\n\n")
    sys.exit(1)
  sys.stdout.flush()

  if ert.options.verbose > 0:
    print()

# When all the experiments have been processed, generate the roofline graph
# and JSON output
if ert.roofline() != 0:
  sys.stderr.write("\n--- Making ERT roofline failed ---\n\n")
  sys.exit(1)

# All done
sys.stdout.flush()
sys.exit(0)
