wait("try_or_install_ubuntu.png", FOREVER)
assert "ubuntu_safe_graphics.png"
type(Key.DOWN)
type(Key.ENTER)

wait("jammy_jellyfish.png", FOREVER)
click("installer_panel_icon.png")

wait("install_ubuntu.png", FOREVER)
click("continue.png")
click("type_here.png")
type("dogflap")
click("continue.png")

assert "use_wired_connection.png"
click("continue.png")

assert "normal_installation.png"
assert "minimal_installation.png"
click("continue.png")

assert "erase_disk.png"
click("continue.png")

assert "write_changes_to_disk.png"

wait("1660739976913.png", FOREVER)
click("start_installing.png")
assert "where_are_you.png"
click("continue.png")

assert "disabled_continue.png"
click("your_name_placeholder.png")
type("Dustin Henderson")
click("1660732897015.png")
type("a", Key.CTRL)

type("Falkor")

click("1660733380533.png")
type("a", Key.CTRL)
type("dustin")

click("1660732634756.png")
type("herptyderp")

click("1660732681771.png")
type("herptyderp")
click("continue.png")

assert("copying_files.png")
wait("1660749559452.png", FOREVER)
click("restart_into_ubuntu.png")

wait("please_remove_installation_medium.png", FOREVER)
type(Key.ENTER)
