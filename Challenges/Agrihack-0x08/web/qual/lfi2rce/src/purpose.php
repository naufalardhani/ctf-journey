<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Include directive</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  </head>
  <body>
    <div class="p-5 mb-4 bg-light rounded-3">
        <div class="container-fluid py-5">
          <h1 class="display-5 fw-bold">Purpose</h1>
          <p class="col-md-8 fs-4">The include directive allows libraries of code to be developed which help to:

ensure that everyone uses the same version of a data layout definition or procedural code throughout a program,
easily cross-reference where components are used in a system,
easily change programs when needed (only one file must be edited), and
save time by reusing data layouts.

Example

An example situation which benefits from the use of an include directive is when referring to functions in a different file. So suppose there is some C source file containing a function add, which is referred to in a second file by first declaring its external existence and type (with a function prototype) as follows:

int add(int, int);

int triple(int x)
{
return add(x, add(x, x));
}

One drawback of this approach is that the function prototype must be present in all files that use the function. Another drawback is that if the return type or arguments of the function are changed, all of these prototypes would need to be updated. Putting the prototype in a single, separate file avoids these issues. Assuming the prototype is moved to the file add.h, the second source file can then become:

#include "add.h"

int triple(int x)
{
return add(x, add(x,x));
}

Now, every time the code is compiled, the latest function prototypes in add.h will be included in the files using them, avoiding potential errors. </p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  </body>
</html>
