=======================================================================
               The OGLE Collection of Variable Stars
          Classical Cepheids in the Large Magellanic Cloud

 I. Soszynski, A. Udalski, M. K. Szymanski, D. Skowron, G. Pietrzynski,
    R. Poleski, P. Pietrukowicz, J. Skowron, P. Mroz, S. Kozlowski,
            L. Wyrzykowski, K. Ulaczyk, and M. Pawlak

=======================================================================
soszynsk@astrouw.edu.pl

This directory contains the OGLE catalog classical Cepheids in the Large
Magellanic Cloud.

The directory structure is as follows:

README            - this file

ident.dat         - identification of stars

cepF.dat          - parameters of fundamental-mode (F) Cepheids
cep1O.dat         - parameters of first-overtone (1O) Cepheids
cep2O.dat         - parameters of second-overtone (2O) Cepheids
cepF1O.dat        - parameters of double-mode F/1O Cepheids
cep1O2O.dat       - parameters of double-mode 1O/2O Cepheids
cepF1O2O.dat      - parameters of a triple-mode F/1O/2O Cepheid
cep1O2O3O.dat     - parameters of triple-mode 1O/2O/3O Cepheids
cep1O3O.dat       - parameters of a double-mode 1O/3O Cepheid
cep2O3O.dat       - parameters of a double-mode 2O/3O Cepheid

phot/I/           - I-band photometry of individual objects
phot/V/           - V-band photometry of individual objects
phot.tar.gz       - gzipped phot/ directory

fcharts/          - finding charts of individual objects

remarks.txt       - remarks on selected objects

pap.pdf           - PDF version of the paper Soszynski et al. (2015),
                    Acta Astron. 65, 297, (arXiv:1601.01318) describing the
                    catalog.


Format of the file ident.dat:
--------------------------------------------------------------------------
 Bytes  Format Units   Description
--------------------------------------------------------------------------
  1- 17  A17   ---     Star's ID
 19- 26  A8    ---     Mode(s) of pulsation
 29- 30  I2    h       Right ascension, equinox J2000.0 (hours)
 32- 33  I2    m       Right ascension, equinox J2000.0 (minutes)
 35- 39  F5.2  s       Right ascension, equinox J2000.0 (seconds)
     41  A1    ---     Declination, equinox J2000.0 (sign)
 42- 43  I2    deg     Declination, equinox J2000.0 (degrees)
 45- 46  I2    arcmin  Declination, equinox J2000.0 (arc minutes)
 48- 51  F4.1  arcsec  Declination, equinox J2000.0 (arc seconds)
 54- 69  A16   ---     OGLE-IV ID
 71- 85  A15   ---     OGLE-III ID
 87-101  A15   ---     OGLE-II ID
103-     A     ---     Other designation (from GCVS)
--------------------------------------------------------------------------

Format of files cepF.dat, cep1O.dat, and cep2O.dat:
--------------------------------------------------------------------------
 Bytes  Format Units   Description
--------------------------------------------------------------------------
  1- 17  A17   ---     Star's ID
 20- 25  F6.3  mag     Intensity mean I-band magnitude
 27- 32  F6.3  mag     Intensity mean V-band magnitude
 34- 44  F11.7 days    Period
 46- 54  F9.7  days    Uncertainty of period
 57- 66  F10.5 days    Time of maximum brightness (HJD-2450000)
 69- 73  F5.3  mag     I-band amplitude (maximum-minimum)
 76- 80  F5.3  ---     Fourier coefficient R_21
 82- 86  F5.3  ---     Fourier coefficient phi_21
 89- 93  F5.3  ---     Fourier coefficient R_31
 95- 99  F5.3  ---     Fourier coefficient phi_31
--------------------------------------------------------------------------

Format of files cepF1O.dat, cep1O2O.dat, cep1O3O.dat, and cep2O3O.dat:
--------------------------------------------------------------------------
 Bytes  Format Units   Description
--------------------------------------------------------------------------
  1- 17  A17   ---     Star's ID
 20- 25  F6.3  mag     Intensity mean I-band magnitude
 27- 32  F6.3  mag     Intensity mean V-band magnitude
 34- 44  F11.7 days    Longer period
 46- 54  F9.7  days    Uncertainty of the longer period
 57- 66  F10.5 days    Time of maximum brightness (HJD-2450000)
 69- 73  F5.3  mag     I-band amplitude (maximum-minimum)
 76- 80  F5.3  ---     Fourier coefficient R_21
 82- 86  F5.3  ---     Fourier coefficient phi_21
 89- 93  F5.3  ---     Fourier coefficient R_31
 95- 99  F5.3  ---     Fourier coefficient phi_31
101-110  F10.7 days    Shorter period
112-120  F9.7  days    Uncertainty of the shorter period
123-132  F10.5 days    Time of maximum brightness (HJD-2450000)
135-139  F5.3  mag     I-band amplitude (maximum-minimum)
142-146  F5.3  ---     Fourier coefficient R_21
148-152  F5.3  ---     Fourier coefficient phi_21
155-159  F5.3  ---     Fourier coefficient R_31
161-165  F5.3  ---     Fourier coefficient phi_31
--------------------------------------------------------------------------

Format of files cepF1O2O.dat and cep1O2O3O.dat:
--------------------------------------------------------------------------
 Bytes  Format Units   Description
--------------------------------------------------------------------------
  1- 17  A17   ---     Star's ID
 20- 25  F6.3  mag     Intensity mean I-band magnitude
 27- 32  F6.3  mag     Intensity mean V-band magnitude
 34- 44  F11.7 days    Longest period
 46- 54  F9.7  days    Uncertainty of the longest period
 57- 66  F10.5 days    Time of maximum brightness (HJD-2450000)
 69- 73  F5.3  mag     I-band amplitude (maximum-minimum)
 76- 80  F5.3  ---     Fourier coefficient R_21
 82- 86  F5.3  ---     Fourier coefficient phi_21
 89- 93  F5.3  ---     Fourier coefficient R_31
 95- 99  F5.3  ---     Fourier coefficient phi_31
101-110  F10.7 days    Medium period
112-120  F9.7  days    Uncertainty of the medium period
123-132  F10.5 days    Time of maximum brightness (HJD-2450000)
135-139  F5.3  mag     I-band amplitude (maximum-minimum)
142-146  F5.3  ---     Fourier coefficient R_21
148-152  F5.3  ---     Fourier coefficient phi_21
155-159  F5.3  ---     Fourier coefficient R_31
161-165  F5.3  ---     Fourier coefficient phi_31
167-176  F10.7 days    Shortest period
178-186  F9.7  days    Uncertainty of the shortest period
189-198  F10.5 days    Time of maximum brightness (HJD-2450000)
201-205  F5.3  mag     I-band amplitude (maximum-minimum)
208-212  F5.3  ---     Fourier coefficient R_21
214-218  F5.3  ---     Fourier coefficient phi_21
221-225  F5.3  ---     Fourier coefficient R_31
227-231  F5.3  ---     Fourier coefficient phi_31
--------------------------------------------------------------------------

Format of the files with photometry (phot/I/OGLE-LMC-CEP-NNNN.dat,
phot/V/OGLE-LMC-CEP-NNNN.dat)
--------------------------------------------------------------------------
 Bytes  Format Units   Description
--------------------------------------------------------------------------
  1- 10  F10.5 days    Heliocentric Julian Day - 2450000
 12- 17  F6.3  mag     Magnitude
 19- 23  F5.3  mag     Uncertainty of magnitude
--------------------------------------------------------------------------


Finding charts are gzipped Postscript images. The names of the files are in
the form: ID.ps.gz. The finding charts are 60"x60" subframes of the I-band
reference frames centered on the star. White cross marks the star. North is
up and East to the left.

Any presentation of the scientific analysis or usage of the data from the
catalog of classical Cepheids in the Magellanic Clouds should include the
appropriate reference(s) to OGLE paper(s).


Updates:

2017-06-30  The collection extended with Cepheids from OGLE-LMC-CEP-4625
            to OGLE-LMC-CEP-4709 detected in the OGLE-IV auxiliary
            photometric databases. Light curves of other objects
            supplemented with new observations. For details see: Soszynski
            et al. (2017), Acta Astron. 67, 103 (arXiv:1706.09452).

2018-06-04  Corrected erroneous calibration of the V-band photometry for
            47 objects.

2018-07-12  Corrected erroneous calibration of the I-band photometry for
            297 objects.
