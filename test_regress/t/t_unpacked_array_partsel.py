#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# SPDX-FileCopyrightText: 2026 Wilson Snyder
# SPDX-License-Identifier: CC0-1.0

import vltest_bootstrap

test.scenarios('simulator')

# Test that part-selects on unpacked array elements compile without
# spurious "Unsupported LHS tristate construct: ARRAYSEL" errors.
# This is a regression test for a false positive in V3Tristate.

test.compile()

test.execute()

test.passes()
