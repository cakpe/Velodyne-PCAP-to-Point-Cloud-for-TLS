# PCAP-to-Point-Cloud-for-TLS
Simple GUI interface that allows converting of PCAP files generated by a VLP-16 lidar to PLY Point clouds

This is based on the work by Jason Bula and his velodyne_tls Matlab script. https://github.com/jason-bula/velodyne_tls
I have created a gui and a stand alone application for it so you do not need Matlab if you use the installer. You will need to download the Matlab 2022a Runtime which is freely avalible at Mathworks: https://www.mathworks.com/products/compiler/matlab-runtime.html
The Stand alone was written to run on a Windows 64 machine and must be installed to C:\TLS_Pie or it will not work. You can change this diretory in the MATLAB files and recompile if you would like to to be installed somewhere else. 

Detailed instructions on the settings and calibration of the unit are at https://github.com/jason-bula/velodyne_tls

![app main screen](https://user-images.githubusercontent.com/15005663/170880929-3ba67ac1-b718-4b3d-9a39-e72b373c682f.png)

The software for the scanner can be found here: https://github.com/Rotoslider/TLS_Pie
