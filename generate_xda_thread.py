#!/usr/bin/env python3
import os
import re
import sys
import calendar
import datetime
import requests

GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
RED = "\033[0;31m"
ENDCOLOR = "\033[0m"


def display_header():
    print(f"{GREEN}==========================================================={ENDCOLOR}")
    print(f"{BLUE}      ______            __      __  _                _  __  {ENDCOLOR}")
    print(f"{BLUE}     / ____/   ______  / /_  __/ /_(_)___  ____     | |/ /  {ENDCOLOR}")
    print(f"{BLUE}    / __/ | | / / __ \\/ / / / / __/ / __ \\/ __ \\    |   /{ENDCOLOR}")
    print(f"{BLUE}   / /___ | |/ / /_/ / / /_/ / /_/ / /_/ / / / /   /   |    {ENDCOLOR}")
    print(f"{BLUE}  /_____/ |___/\\____/_/\\__,_/\\__/_/\\____/_/ /_/   /_/|_|{ENDCOLOR}")
    print(f"{BLUE}                                                            {ENDCOLOR}")
    print(f"{BLUE}                     XDA thread generator                   {ENDCOLOR}")
    print(f"{BLUE}                                                            {ENDCOLOR}")
    print(f"{BLUE}                         #KeepEvolving                      {ENDCOLOR}")
    print(f"{GREEN}==========================================================={ENDCOLOR}")

def input_nonempty(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data

def generate_thread():
    os.system("clear")
    display_header()

    # Device manufacturer
    while True:
        manufacturer = input("Manufacturer name: ").strip()
        if re.search(r"\d", manufacturer):
            print("Manufacturer name should not contain numbers. Please try again.")
            continue
        else:
            break

    manufacturer_lowercase = manufacturer.lower()

    if manufacturer_lowercase == "google":
        manufacturer_name = "[SIZE=6][B][COLOR=rgb(0, 96, 255)]G[/COLOR][COLOR=rgb(184, 49, 47)]o[/COLOR][COLOR=rgb(250, 197, 28)]o[/COLOR][COLOR=rgb(0, 96, 255)]g[/COLOR][COLOR=rgb(97, 189, 109)]l[/COLOR][COLOR=rgb(184, 49, 47)]e[/COLOR][/B][/SIZE]"
    elif manufacturer_lowercase == "oneplus":
        manufacturer_name = (
            "[B][COLOR=rgb(226, 80, 65)][SIZE=6]OnePlus[/SIZE][/COLOR][/B]"
        )
    elif manufacturer_lowercase == "xiaomi":
        manufacturer_name = (
            "[B][COLOR=rgb(251, 160, 38)][SIZE=6]Xiaomi[/SIZE][/COLOR][/B]"
        )
    else:
        # Capitalize first letter
        manufacturer_name = f"[B][COLOR=rgb(0, 96, 255)][SIZE=6]{manufacturer[0].upper()}{manufacturer[1:]}[/SIZE][/COLOR][/B]"

    # Device name & codename
    print("Device names (separated by ',' and/or '&' e.g Pixel 7, 7 Pro & 7a): ")
    devices = input().strip()
    # Remove extra spacing around separators
    devices = re.sub(r"\s*([,&])\s*", r"\1", devices)
    # Split by , or &
    device_array = re.split(r"[,&]", devices)
    device_array = [dev.strip() for dev in device_array if dev.strip()]
    device_count = len(device_array)

    if device_count == 1:
        device = device_array[0]
        device_name = f"[COLOR=rgb(0, 96, 255)][B][SIZE=6]{device}[/SIZE][/B][/COLOR]"
        codename = input(f"Codename for {device}: ").strip()
        codenames = f"[COLOR=rgb(0, 96, 255)][B][SIZE=6][{codename}][/SIZE][/B][/COLOR]"
    else:
        device_name = "[COLOR=rgb(0, 96, 255)][B][SIZE=6]"
        codenames = "[COLOR=rgb(0, 96, 255)][B][SIZE=6]"
        for i, device in enumerate(device_array):
            device = device.strip()
            device_name += device
            codename = input(f"Codename for {device}: ").strip()
            codenames += f"[{codename}]"
            if i != device_count - 1:
                if i == device_count - 2:
                    device_name += " & "
                else:
                    device_name += ", "
        device_name += "[/SIZE][/B][/COLOR]"
        codenames += "[/SIZE][/B][/COLOR]"

    # Banner styles
    banner_options = {
        "1": "banner_style_1.png",
        "2": "banner_style_2.png",
        "3": "banner_style_3.png",
        "4": "banner_style_4.png",
        "5": "banner_style_5.png",
    }
    while True:
        print("Choose the banner style:")
        print("1. Center punch-hole notch")
        print("2. Left side punch-hole notch")
        print("3. No notch")
        print("4. Pop up camera")
        print("5. Tablet")
        banner_choice = input("Enter your choice (1-5): ").strip()
        if banner_choice in banner_options:
            banner_image = banner_options[banner_choice]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Security patch URL/Name
    while True:
        security_patch_level = input("Security patch level (mm/yyyy): ").strip()
        if re.match(r"^\d{2}/\d{4}$", security_patch_level):
            patch_month_str, patch_year_str = security_patch_level.split("/")
            patch_month = int(patch_month_str)
            patch_year = int(patch_year_str)
            if 1 <= patch_month <= 12:
                patch_month_full = calendar.month_name[patch_month]
                security_patch_level_date = f"{patch_month_full} {patch_year}"
                security_patch_url = f"https://source.android.com/security/bulletin/{patch_year}-{patch_month_str}-01"
                current_date = int(datetime.datetime.now().strftime("%Y%m"))
                provided_date = patch_year * 100 + patch_month
                if provided_date <= current_date:
                    break
                else:
                    print(
                        f"{RED}The provided date is in the future. Please enter a valid date.{ENDCOLOR}"
                    )
            else:
                print(
                    f"{RED}Month out of range. Please enter a valid month (01-12).{ENDCOLOR}"
                )
        else:
            print(
                f"{RED}Invalid format or out of range. Please use mm/yyyy format with a valid month and year.{ENDCOLOR}"
            )

    # XDA second post URL
    pattern_xda_thread = r"^https://xdaforums\.com/t/"
    while True:
        installation_images_url = input(
            "XDA thread second post URL (this is where your download links should reside): "
        ).strip()
        if re.match(pattern_xda_thread, installation_images_url):
            break
        else:
            print(
                f"{RED}Invalid format. Please enter a URL starting with 'https://xdaforums.com/t/'.{ENDCOLOR}"
            )

    # Manifest URL & Android version
    while True:
        try:
            r = requests.get(
                "https://api.github.com/repos/Evolution-X/manifest/branches"
            )
            branches_json = r.json()
            branches = [branch["name"] for branch in branches_json]
        except Exception as e:
            print(f"{RED}Failed to fetch branches: {e}{ENDCOLOR}")
            sys.exit(1)

        print("Available branches:")
        for index, branch in enumerate(branches):
            print(f"{index+1}) {branch}")

        branch_index = input(
            "Select the manifest branch used for compilation: "
        ).strip()
        if (
            not branch_index.isdigit()
            or int(branch_index) < 1
            or int(branch_index) > len(branches)
        ):
            print(
                f"{RED}Invalid selection. Please enter a valid option (1-{len(branches)}).{ENDCOLOR}"
            )
            continue

        selected_branch = branches[int(branch_index) - 1]
        raw_manifest_url = f"https://raw.githubusercontent.com/Evolution-X/manifest/{selected_branch}/default.xml"
        xml_response = requests.get(raw_manifest_url)
        xml_data = xml_response.text

        tree_url = f"https://github.com/Evolution-X/manifest/tree/{selected_branch}"

        if xml_data:
            m = re.search(r'revision="refs/tags/android-([^"]+)"', xml_data)
            if m:
                android_version = m.group(1)
                print(f"{GREEN}Android version detected: {android_version}{ENDCOLOR}")
                break
            else:
                print(f"{RED}Android version not found in the XML.{ENDCOLOR}")
        else:
            print(f"{RED}Failed to fetch XML data from {raw_manifest_url}.{ENDCOLOR}")

    # Kernel source URL
    kernel_pattern = r"^(https?://)?(www\.)?(github\.com|gitlab\.com|bitbucket\.org|git\.com|android\.googlesource\.com)(.*)"
    while True:
        kernel_source_url = input("Kernel Source URL: ").strip()
        if re.match(kernel_pattern, kernel_source_url):
            break
        else:
            print(
                f"{RED}Invalid format. Please enter a valid URL from GitHub, GitLab, Bitbucket, or any other Git hosting service.{ENDCOLOR}"
            )

    # Clang version
    while True:
        clang_version = input("Clang Version: ").strip()
        if re.match(r"^[0-9]+(\.[0-9]+)*$", clang_version):
            break
        else:
            print(
                f"{RED}Invalid format. Please enter a Clang version in the format of only numbers with optional decimal points (e.g., 14.0.7).{ENDCOLOR}"
            )

    # Maintainer name
    while True:
        maintainer_name = input("Your full name: ").strip()
        if not re.search(r"\d", maintainer_name):
            break
        else:
            print(
                f"{RED}Invalid name. Please enter your full name without numbers.{ENDCOLOR}"
            )

    # XDA profile URL
    xda_profile_pattern = r"^https://xdaforums\.com/m/[A-Za-z0-9._%-]+\.[0-9]+/"
    while True:
        xda_profile_url_full = input("XDA profile URL: ").strip()
        if re.match(xda_profile_pattern, xda_profile_url_full):
            break
        else:
            print(
                f"{RED}Invalid format. Please enter a URL in the format: https://xdaforums.com/m/username.123456/{ENDCOLOR}"
            )

    # Extract username from URL (second last section)
    parts = xda_profile_url_full.rstrip("/").split("/")
    if len(parts) >= 2:
        xda_username = parts[-1] if parts[-1] else parts[-2]
    else:
        xda_username = ""
    xda_profile_url = f"https://xdaforums.com/m/{xda_username}/"

    # Donation URL
    while True:
        donation_url = input("Donation URL: ").strip()
        if re.match(r"^https?://", donation_url):
            break
        else:
            print(
                f"{RED}Invalid format. Please enter a valid URL starting with 'http://' or 'https://'.{ENDCOLOR}"
            )

    # Prepare the thread content
    thread_content = f"""[CENTER]
{manufacturer_name} {device_name}
{codenames}

[IMG]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/{banner_image}[/IMG]

[SIZE=5][B][COLOR=#0060FF][B]Pixel UI, customization and more, we are Evolution X![/B][/COLOR][/B][/SIZE]

[URL='https://xdaforums.com/m/joeyhuab.4936496/']Joey Huab[/URL] - Founder/Lead Developer
[URL='https://xdaforums.com/m/anierinb.7125966/']Anierin Bliss[/URL] - Co-Founder/Co-Developer
[URL='https://xdaforums.com/m/realakito.9008281/']Akito Mizukito[/URL] - Co-Founder/Project Manager

[I]Reach us on Twitter! [URL='https://twitter.com/EvolutionXROM']@EvolutionXROM[/URL][/I]
Check out our [URL='https://evolution-x.org/']website[/URL]!

[IMG]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/features.png[/IMG]

[URL='https://github.com/Evolution-X/XDA/blob/udc/features.md']Added features[/URL]

[IMG]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/known_issues.png[/IMG]

[SIZE=5][B][COLOR=red]DO NOT FLASH GAPPS, THEY ARE ALREADY INCLUDED[/COLOR][/B][/SIZE]

[B][IMG]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/installation.png[/IMG][/B]

[SPOILER]
[SIZE=5][B][COLOR=rgb(0, 96, 255)][SIZE=5][B]First Time Install[/B][/SIZE][/COLOR][/B][/SIZE]
[COLOR=rgb(251, 160, 38)](Note: These releases include firmware)[/COLOR]
1. Download boot, dtbo, vendor_kernel_boot, vendor_boot & rom for your device from [URL='{installation_images_url}']here[/URL]
2. Reboot to bootloader
3. fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash vendor_kernel_boot vendor_kernel_boot.img
fastboot flash vendor_boot vendor_boot.img
fastboot reboot recovery
4. While in recovery, navigate to Factory reset -> Format data/factory reset and confirm to format the device.
5. When done formatting, go back to the main menu and then navigate to Apply update -> Apply from ADB
6. adb sideload rom.zip (replace "rom" with actual filename)
7 (optional). Reboot to recovery (fully) to sideload any add-ons (e.g magisk)
8. Reboot to system & #KeepEvolving

[SIZE=5][B][COLOR=rgb(0, 96, 255)]Update[/COLOR][/B][/SIZE]
[SIZE=3]1. Reboot to recovery
2. While in recovery, navigate to Apply update -> Apply from ADB
3. adb sideload rom.zip (replace "rom" with  actual filename)[/SIZE]
4 (optional). Reboot to recovery to sideload any add-ons (e.g magisk)
[SIZE=3]5. Reboot to system & #KeepEvolving

[COLOR=rgb(0, 96, 255)][SIZE=5][B]OTA[/B][/SIZE][/COLOR]
[SIZE=3]1. Check for update. If available, select "Download and install" (approx 10-15 min)
2. Reboot & #KeepEvolving[/SIZE]
[/SPOILER]

[URL='{donation_url}'][IMG width="200px" height="180px"]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/donate_to_me.png[/IMG][/URL][URL='https://discord.gg/3qbSZHx'][IMG width="200px" height="180px"]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/official_chat.png[/IMG][/URL][/CENTER]

[TABLE]
[TR]
[TD][IMG]https://raw.githubusercontent.com/Evolution-X/XDA/udc/assets/source.png[/IMG][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(97, 189, 109)]Android version[/COLOR]:[/B] [URL='{tree_url}']{android_version}[/URL][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(184, 49, 47)]Security patch level[/COLOR]:[/B] [URL='{security_patch_url}']{security_patch_level_date}[/URL][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(41, 105, 176)]Build author[/COLOR]:[/B] [URL='{xda_profile_url}']{maintainer_name}[/URL][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(65, 168, 95)]Kernel Source[/COLOR]:[/B] [URL]{kernel_source_url}[/URL][/TD]
[/TR]
[TR]
[TD][COLOR=rgb(243, 121, 52)][B]Clang version:[/B] {clang_version}[/COLOR][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(41, 105, 176)]ROM Developer[/COLOR]:[/B] [URL='https://xdaforums.com/member.php?u=4936496']Joey Huab[/URL] & [URL='https://xdaforums.com/m/anierinb.7125966/']Anierin Bliss[/URL][/TD]
[/TR]
[TR]
[TD][B][COLOR=rgb(97, 189, 109)]Source code[/COLOR]:[/B] [URL]https://github.com/Evolution-X[/URL][/TD]
[/TR]
[/TABLE]
[CENTER][/CENTER]"""

    # Write content to temporary file
    output_folder = "out"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, "generated_xda_thread.txt")
    try:
        with open(output_path, "w") as f:
            f.write(thread_content)
        print(f"{GREEN}Thread saved to '{output_path}'{ENDCOLOR}")
    except Exception as e:
        print(f"{RED}Error saving thread: {e}{ENDCOLOR}")
        sys.exit(1)

if __name__ == "__main__":
    generate_thread()
