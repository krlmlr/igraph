/*
   igraph library.
   Copyright (C) 2025  The igraph development team <igraph@igraph.org>

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

#include <igraph.h>

#include "test_utilities.h"

int main(void) {

    /* Test that igraph_setup() succeeds */
    IGRAPH_ASSERT(igraph_setup() == IGRAPH_SUCCESS);
    printf("igraph_setup() succeeded.\n");

    /* Test that igraph_setup() can be called multiple times */
    IGRAPH_ASSERT(igraph_setup() == IGRAPH_SUCCESS);
    printf("igraph_setup() second call succeeded.\n");

    /* After setup, the RNG should be seeded and usable. */
    igraph_rng_t *rng = igraph_rng_default();
    IGRAPH_ASSERT(rng != NULL);
    /* Verify the RNG is functional by generating a random number */
    igraph_int_t val = igraph_rng_get_integer(rng, 0, 100);
    IGRAPH_ASSERT(val >= 0 && val <= 100);
    printf("RNG is seeded after igraph_setup().\n");

    VERIFY_FINALLY_STACK();

    return 0;
}
