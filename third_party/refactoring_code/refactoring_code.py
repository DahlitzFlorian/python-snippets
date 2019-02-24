from rope.refactor import change_signature
import testutils


project = testutils.sample_project()
pycore = project.pycore
mod = testutils.create_module(project, "mod")

code = (
    "class A(object):\n"
    "    def a_func(self, param):\n"
    "        pass\n"
    "a_var = A()\n"
    "a_var.a_func(param=1)\n"
)

mod.write(code)
signature = change_signature.ChangeSignature(
    project, mod, mod.read().index("a_func") + 1
)
project.do(signature.get_changes([change_signature.ArgumentNormalizer()]))
expected = (
    "class A(object):\n"
    "    def a_func(self, param):\n"
    "        pass\n"
    "a_var = A()\n"
    "a_var.a_func(1)\n"
)

print("==================== Before Refactoring ====================")
print(code)
print("==================== After Refactoring =====================")
print(mod.read())
