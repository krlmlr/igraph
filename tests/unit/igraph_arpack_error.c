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

#include <string.h>

int main(void) {
    const char *msg;

    /* Test igraph_arpack_error_to_string for all known error codes */
    printf("Testing igraph_arpack_error_to_string():\n");

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NO_ERROR);
    IGRAPH_ASSERT(msg != NULL);
    IGRAPH_ASSERT(strcmp(msg, "No error") == 0);
    printf("  NO_ERROR: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_PROD);
    IGRAPH_ASSERT(msg != NULL);
    printf("  PROD: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NPOS);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NPOS: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NEVNPOS);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NEVNPOS: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NCVSMALL);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NCVSMALL: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NONPOSI);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NONPOSI: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_WHICHINV);
    IGRAPH_ASSERT(msg != NULL);
    printf("  WHICHINV: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_BMATINV);
    IGRAPH_ASSERT(msg != NULL);
    printf("  BMATINV: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_WORKLSMALL);
    IGRAPH_ASSERT(msg != NULL);
    printf("  WORKLSMALL: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_TRIDERR);
    IGRAPH_ASSERT(msg != NULL);
    printf("  TRIDERR: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_ZEROSTART);
    IGRAPH_ASSERT(msg != NULL);
    printf("  ZEROSTART: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_MODEINV);
    IGRAPH_ASSERT(msg != NULL);
    printf("  MODEINV: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_MODEBMAT);
    IGRAPH_ASSERT(msg != NULL);
    printf("  MODEBMAT: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_ISHIFT);
    IGRAPH_ASSERT(msg != NULL);
    printf("  ISHIFT: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NEVBE);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NEVBE: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NOFACT);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NOFACT: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_FAILED);
    IGRAPH_ASSERT(msg != NULL);
    printf("  FAILED: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_HOWMNY);
    IGRAPH_ASSERT(msg != NULL);
    printf("  HOWMNY: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_HOWMNYS);
    IGRAPH_ASSERT(msg != NULL);
    printf("  HOWMNYS: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_EVDIFF);
    IGRAPH_ASSERT(msg != NULL);
    printf("  EVDIFF: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_SHUR);
    IGRAPH_ASSERT(msg != NULL);
    printf("  SHUR: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_LAPACK);
    IGRAPH_ASSERT(msg != NULL);
    printf("  LAPACK: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_UNKNOWN);
    IGRAPH_ASSERT(msg != NULL);
    printf("  UNKNOWN: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_MAXIT);
    IGRAPH_ASSERT(msg != NULL);
    printf("  MAXIT: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_NOSHIFT);
    IGRAPH_ASSERT(msg != NULL);
    printf("  NOSHIFT: %s\n", msg);

    msg = igraph_arpack_error_to_string(IGRAPH_ARPACK_REORDER);
    IGRAPH_ASSERT(msg != NULL);
    printf("  REORDER: %s\n", msg);

    /* Test unknown error code (not in enum) returns valid string */
    msg = igraph_arpack_error_to_string((igraph_arpack_error_t) 99);
    IGRAPH_ASSERT(msg != NULL);
    IGRAPH_ASSERT(strcmp(msg, "Unknown ARPACK error") == 0);
    printf("  Out-of-range: %s\n", msg);

    /* Test igraph_arpack_get_last_error - should return NO_ERROR initially */
    printf("\nTesting igraph_arpack_get_last_error():\n");
    igraph_arpack_error_t last_error = igraph_arpack_get_last_error();
    printf("  Initial last error: %d\n", (int) last_error);

    /* Test igraph_strerror for new error codes */
    printf("\nTesting igraph_strerror() with new error codes:\n");

    msg = igraph_strerror(IGRAPH_EARPACK);
    IGRAPH_ASSERT(msg != NULL);
    printf("  IGRAPH_EARPACK: %s\n", msg);

    msg = igraph_strerror(IGRAPH_EINVEID);
    IGRAPH_ASSERT(msg != NULL);
    printf("  IGRAPH_EINVEID: %s\n", msg);

    VERIFY_FINALLY_STACK();

    return 0;
}
