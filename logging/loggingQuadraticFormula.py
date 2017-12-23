import logging
import math


# Create and configure logger

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logging.log",level = logging.DEBUG,
	format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

# Test the logger
logger.info("our fist message")

def quadratic_formual(a, b, c):
	"""Return the soulution to the equation ax^2 + bx + c =0."""
	logger.info("quadratic_formaul({0},{1},{2})".format(a, b, c))
	# Compute the discriminant
	logger.debug("# Compute the discriminant")
	disc = b**2 - 4*a*c
	print id(disc)

	# Compute the two roots
	logger.debug("# Compute the two roots")
	root1 = (-b+math.sqrt(disc)) / (2*a)
	root2 = (-b-math.sqrt(disc)) / (2*a)

	# Return the roots
	logger.debug(" # Return the roots")
	return(root1,root2)

roots = quadratic_formual(1, 0, -1)
print(roots)





