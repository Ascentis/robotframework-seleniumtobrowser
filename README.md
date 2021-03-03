# robotframework-seleniumtobrowser
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## Introduction

Robot Framework SeleniumToBrowser library helps with converting automated tests using [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary) keywords to [Browser](https://github.com/MarketSquare/robotframework-browser) library


## Usage

A couple of considerations on how to use this library:
- Both Browser and SeleniumToBrowser must be declared inside the robot code.
- "Overlapping keywords" between Selenium and Brower, like Open Browser will need to called with the library prefix
