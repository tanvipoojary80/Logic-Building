# Pattern - 2
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *

n = 5 # size

# Top half
for i in range(n, 0, -1):
    # left stars
    print("* " * i, end="")
    # middle spaces
    print("  " * (2 * (n - i)), end="")
    # right stars
    print("* " * i)

# Bottom half
for i in range(1, n + 1):
    # left stars
    print("* " * i, end="")
    # middle spaces
    print("  " * (2 * (n - i)), end="")
    # right stars
    print("* " * i)

# output:
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *