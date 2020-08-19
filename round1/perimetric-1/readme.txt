After a highly successful haul from the log drive, Connie the contractor is
tasked with building a number of houses in the Great White North. For each job,
the client has provided a floor plan consisting of N rectangular rooms,
numbered from 1 to N. From a bird's-eye view, the rooms are arranged on a
2-dimensional plane, with axis-aligned walls. The southern wall of each room has
y-coordinate 0.

Unfortunately, log houses are quite susceptible to air leakage. Connie knows
that she must install additional insulation to keep the houses warm and
energy-efficient during the harsh Canadian winters. In order to determine the
amount of insulation material required, Connie will first need to gather some
metrics: the perimeters around various combinations of rooms.

Specifically, let P_i be the perimeter of the union of rooms 1..i. Note that any
given point is considered to be within the union if and only if it's within at
least one of the rooms' rectangles (including right on an edge), and that the
union might not form a single connected polygon. Please help compute the product
(P_1 * P_2 * ... * P_N). As this product may be very large, you should compute
its value modulo 1,000,000,007.
