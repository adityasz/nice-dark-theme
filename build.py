#!/usr/bin/env python3

import sublate as sub

sub.data.update({"colors": sub.read("colors/*.yaml").values()})

for theme in sub.data["colors"]:
    sub.render(f"resources/theme/{theme['id']}.theme.json",
               "template/theme.json", {"theme": theme})
