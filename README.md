# 📦CratCAL - An easy-to-use crate calculator 📈

---

![sample](\example.png)


## Table of Contents

---

- [📦CratCAL - An easy-to-use crate calculator 📈](#cratcal---an-easy-to-use-crate-calculator-)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Installation](#installation)
    - [Raspberry Pi](#raspberry-pi)
    - [Windows](#windows)
    - [Android](#android)
  - [Rundown](#rundown)
  - [**Possible changes in the future**](#possible-changes-in-the-future)





## Overview

---

`CratCAL` is a small Python script for accurately calculating the missing crates needed for empty running the production line 4.
It helps the user to get faster and reliable to needed information.
This also minimize the error of overfilling the magazine and needlessly extending the time to empty run the production line.

It's lightweight, easy to use and should run on anything that can handle .py files.
`CratCAL` is also tested and useable on Android phones via the [Pydroid 3 IDE][Pydroid3].

## Installation

---

`CratCAL` is focused to run on a [Raspberry Pi](#raspberry-pi) (Linux), but you can run it on [Windows](#windows) or [Android](#android) too.

### Raspberry Pi

1. Navigate to `/home/pi/` on your Raspberry Pi and put the `CratCAL.py` script in it.
2. Now you have to open the `.bashrc` file that is also located in the directory.
3. Add the following code at the end of the file and save it:
   ```
   echo Running at boot 
   sudo python /home/pi/CratCAL.py
   ```
4. Restart the Raspberry Pi and the `CratCAL` script execute on boot up.
---
### Windows

1. Go to the [Python][Python3] download page and download the latest Python 3 version.
2. Take the steps through the installer.
3. Now you can execute the `CratCAL.py` via Python 3, and it should look like the pictures in [Rundown](#rundown).

---
### Android

>***INFO:***
**This is NOT the intended way of using `CratCAL`!**
Used lib's in the script will **NOT WORK PROBABLY** and can throw error's out in terminal!

**1.** Go to the Google Play Store and download/install [Pydroid 3][Pydroid3].
**2.** Open it on your phone, navigate to the `Folder` icon on the top right.
  
  ![Pydroid3.1](\Pydroid1.png)

**3.** Click `Open` and search for the `CrateCAL.py` script and open it.
   
   ![Pydroid3.2](\Pydroid2.png)

**4.** After loading up the script, you can run it via the yellow `Play button`
   
   ![Pydroid3.3](\Pydroid3.png)

**5.** Now you can use it like on the other devices.
   
   ![Pydroid3.4](\Pydroid5.png)

  

## Rundown

---

**1.** On startup, `CratCAL` asks for the value of currently stored crates.
The user have to check for this value and enter it, in this case `1080`

![Rd.1](\1.png)

**2.** Now you can see the calculated values. There meaning is as following:
- Stored crates in %. (`40%`)
- Needed crates/hub to reach 85%. (`1246 crates` , `6 Hub` , `5.8 Hub` true value)
- Needed crates/hub to reach 100%. (`1656 crates` , `8 Hub` , `7.7 Hub` true value)

![Rd.2](\2.png)

>***INFO:***  
`CratCAL` shows the **raised amount of crates** needed to reach 85% and 100%.
It also convert it in Hub needed, so the missing crates can easily be ordered.  
**The number for Hub needed always get raised to the next larger number (if decimal)**, so it is guaranteed 
that there are always enough crates.  
For double-checking reasons the **true value for Hub needed is in brackets**.

**3.** In the last step, `CratCAL` asks if you want to restart. If so, press 1.
Keep in mind that the screen clears after restarting.
 

---

## **Possible changes in the future**

- [ ] Develop GUI for user inputs via Touchscreen
- [ ] Communication Raspberry Pi and Siemens SPS (Automatically get current state of magazine)
- [ ] Adding additional language for more accessibility 






[Pydroid3]: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&gl=DE
[Python3]: https://www.python.org/downloads/