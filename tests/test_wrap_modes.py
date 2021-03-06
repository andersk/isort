from hypothesis_auto import auto_pytest_magic

from isort import wrap_modes

auto_pytest_magic(wrap_modes.grid, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.vertical, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.hanging_indent, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.vertical_hanging_indent, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.vertical_grid, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.vertical_grid_grouped, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.vertical_grid_grouped_no_comma, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.noqa, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(wrap_modes.noqa, auto_allow_exceptions_=(ValueError,), comments=["NOQA"])
auto_pytest_magic(
    wrap_modes.vertical_prefix_from_module_import, auto_allow_exceptions_=(ValueError,)
)
auto_pytest_magic(wrap_modes.vertical_hanging_indent_bracket, auto_allow_exceptions_=(ValueError,))
auto_pytest_magic(
    wrap_modes.vertical_hanging_indent_bracket,
    auto_allow_exceptions_=(ValueError,),
    imports=["one", "two"],
)


def test_wrap_mode_interface():
    assert (
        wrap_modes._wrap_mode_interface("statement", [], "", "", 80, [], "", "", True, True) == ""
    )
