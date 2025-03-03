# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from DcgmiDiag import DcgmiDiag
import utils

def main():
    dd = DcgmiDiag(dcgmiPrefix=utils.verify_binary_locations())
    passedCount = 0
    for i in range(0, 160):
        print("&&&& RUNNING dcgmi_diag_test")
        failed = dd.Run()
        if failed:
            print("&&&& FAILED dcgmi_diag_test")
            dd.PrintLastRunStatus()
        else:
            print("&&&& PASSED dcgmi_diag_test")
            passedCount += 1

if __name__ == '__main__':
    main()
