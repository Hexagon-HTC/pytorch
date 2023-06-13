#include <operator_registry.h>
#include "${fn_header}" // Generated Function import headers

namespace torch {
namespace executor {

namespace {
using KernelArrayRef = ::at::ArrayRef<::torch::executor::Kernel>;

static Kernel operators_to_register[] = {
    ${unboxed_kernels} // Generated operators
};

// Explicitly convert to ArrayRef, so that the API can take an empty C array of
// Kernels.
static KernelArrayRef kernel_array_ref(
    kernels_to_register,
    kernels_to_register + sizeof(kernels_to_register) / sizeof(Kernel));

// Return value not used. Keep the static variable assignment to register
// operators in static initialization time.
static auto success_with_kernel_reg = register_kernels(kernel_array_ref);
} // namespace
} // namespace executor
} // namespace torch
