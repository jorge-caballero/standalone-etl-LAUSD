<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![AGPL-3.0 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jorge-caballero/standalone-etl-LAUSD">
    <img src="images/logo.png" alt="Logo" width="96" height="96">
  </a>

  <h3 align="center">LAUSD COVID-19 Dashboard Standalone Data Pipeline</h3>

  <p align="center">
    Standalone version of the data pipelines used to retrieve data from the Los Angeles Unified School District (LAUSD) COVID-19 Dashboard, and transform it into CSVs for use in other projects.
    <br />
    <a href="https://github.com/jorge-caballero/standalone-etl-LAUSD"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://dashboard.parentssupportingteachers.org/#">View Demo Usage</a>
    · -->
    <a href="https://github.com/jorge-caballero/standalone-etl-LAUSD/issues">Report Bug</a>
    |
    <a href="https://github.com/jorge-caballero/standalone-etl-LAUSD/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a standalone version of the data pipelines used to retrieve data from the Los Angeles Unified School District (LAUSD) COVID-19 Dashboard, and transform it into CSVs for use in other projects.

[![Example usage Screen Shot][demo-screenshot]](https://dashboard.parentssupportingteachers.org/#)
_An example of how the data generated by this tool is used in the real-world: [@herf](https://github.com/herf/la-covid)'s [LAUSD COVID-19 Dashboard](https://dashboard.parentssupportingteachers.org/#)_


### Built With

* [Python 3](https://www.python.org)
* [jq](https://stedolan.github.io/jq/)
* [pandas](https://pandas.pydata.org)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3 binaries, if missing from your workstation, can be downloaded [here](https://www.python.org/downloads/). Note: you're better off setting up virtual environments (e.g. [pyenv](https://github.com/pyenv/pyenv))
* Python dependencies are listed in the [requirements.txt](https://github.com/jorge-caballero/standalone-etl-LAUSD/blob/main/requirements.txt) file. Once you clone the repo to your local workstation, you can also `cd` into the local folder and run in your terminal:
  ```sh
  cat requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jorge-caballero/standalone-etl-LAUSD.git
   ```
2. Install dependencies
   ```sh
   Makefile init
   ```



<!-- USAGE EXAMPLES -->
## Usage

This is a standalone app with a command-line interface. To get started, simply run the following command:
   ```sh
   python main.py --help
   ```
Here's an example of the command-line options (as of the initial release)
[![CLI help Screen Shot][cli-screenshot]]


_For an example of how the data generated by this tool is used in the real-world, check out [@herf](https://github.com/herf/la-covid)'s [LAUSD COVID-19 Dashboard](https://dashboard.parentssupportingteachers.org/#)_



<!-- ROADMAP -->
## Roadmap

- See [this project](https://github.com/jorge-caballero/standalone-etl-LAUSD/projects/1) for a list of proposed and planned updates
- Check out [issues](https://github.com/jorge-caballero/standalone-etl-LAUSD/issues) for a list of known issues (and pending fixes)



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the AGPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jorge A. Caballero, MD - [@DataDrivenMD](https://twitter.com/DataDrivenMD) - brays[dot]quavers[dot]0t[at]icloud[dot]com

Project Link: [https://github.com/jorge-caballero/standalone-etl-LAUSD](https://github.com/jorge-caballero/standalone-etl-LAUSD)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [@herf](https://github.com/herf) for putting the data into good use. Make sure to check out his [L.A. COVID repo](https://github.com/herf/la-covid), which includes more sources of COVID-19 data for the greater Los Angeles metro area
* [@othneildrew](https://github.com/othneildrew) for the awesome [README template](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)
* [Parents Supporting Teachers](https://twitter.com/pst4lapubliced) for using the data to [advocate on behalf of students and teachers](https://www.latimes.com/california/story/2021-08-23/frustrated-with-lausds-covid-19-reporting-system-a-parent-group-creates-their-own)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jorge-caballero/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/jorge-caballero/standalone-etl-LAUSD/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jorge-caballero/repo.svg?style=for-the-badge
[forks-url]: https://github.com/jorge-caballero/standalone-etl-LAUSD/network/members
[stars-shield]: https://img.shields.io/github/stars/jorge-caballero/repo.svg?style=for-the-badge
[stars-url]: https://github.com/jorge-caballero/standalone-etl-LAUSD/stargazers
[issues-shield]: https://img.shields.io/github/issues/jorge-caballero/repo.svg?style=for-the-badge
[issues-url]: https://github.com/jorge-caballero/standalone-etl-LAUSD/issues
[license-shield]: https://img.shields.io/github/license/jorge-caballero/repo.svg?style=for-the-badge
[license-url]: https://github.com/jorge-caballero/standalone-etl-LAUSD/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/datadrivenmd
[demo-screenshot]: images/ExampleUsage-Dashboard.png
[cli-screenshot]: images/CommandLineScreenShot.png