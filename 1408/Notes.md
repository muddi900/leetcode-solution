# Python

- HashMap based solution solves all test cases(e1cafae21233179e285135c861ffc747f3988454).
- Solution is fairly fast but still at 93 percentile(3d6640f93a7c515a3f4fe8bd3dccc6672ef710a4). Clearly I am being naive somewhere.
- The issue seems to be actual string matching, which is very slow.
- Sorting fixes the speed issue. The approach as not changed but sorting(2679a7c716ea81d6ed1c98a884d582e3d9df45f7).