import open3d as o3d
import os
import numpy as np

# Specify the directory containing the individual PLY files
inputDirectory = 'pointClouds/'

# List all PLY files in the input directory
ply_files = [f for f in os.listdir(inputDirectory) if f.endswith('.ply')]

# Initialize a list to store the loaded point clouds
Cloud = []

# Loop through each PLY file and load it as a point cloud
for ply_file in ply_files:
    # Load the PLY file
    pcd = o3d.io.read_point_cloud(os.path.join(inputDirectory, ply_file))
    
    # Append the loaded point cloud to the list
    Cloud.append(pcd)

# SETTINGS
pos2 = 0
puck = 2
times = 688 # arbitrary nuimber due to Donny's script

# Initialization of export params
if pos2 == 1 and puck == 1:
    bandNumber = 16 #selects all VLP16 segments
elif pos2 == 1 and puck == 2:
    bandNumber = 32 #selects all VLP32C segments
elif pos2 == 0:
    bandNumber = 2 #selects first and last segment [what we select]
elif pos2 == 2:
    bandNumber = 1 #selects middle segment

# Point cloud merging
for bande_sep in range(1, bandNumber + 1):
    if pos2 == 1:
        iiii=bande_sep
    elif pos2 == 0 and puck == 1:
        Bande_calibration = [1, 16]
        iiii = Bande_calibration[bande_sep-1]
    if pos2 == 0 and puck == 2: # where we fall into
        Bande_calibration = [1, 32]
        iiii = Bande_calibration[bande_sep-1]
    if pos2 == 2 and puck == 1:
        Bande_calibration = 8
        iiii = Bande_calibration
    if pos2 == 2 and puck == 2:
        Bande_calibration = 16
        iiii = Bande_calibration

    # Variable initialization
    x = []
    y = []
    z = []
    intensity = []

    X_ref = []
    Y_ref = []
    Z_ref = []
    int_ref = []

    X_ref_final = []
    Y_ref_final = []
    Z_ref_final = []
    int_ref_final = []

    # Acceleration of the process by combining several loops
    for iii in range(1, 11): # from 1 to 10
        for ii in range( (round((times/10*iii)-((times/10)-1))), ((round(iii*times/10))) ): # This range is procesing batches of size 360
            for i in range(iiii, iiii+1): # save the band separately
                # Deleting old values
                x1 = []
                y1 = []
                z1 = []
                int1 = []
                # Selection of points in the correct matrix locations
                # Point clouds are recorded as follows: 16*1800*3
                # 16 corresponds to the band, 1800 corresponds to the number of points recorded
                # per band, 3 corresponds to the x, y and z values.

                x1.append(Cloud[ii].points[i][0])
                y1.append(Cloud[ii].points[i][1])
                z1.append(Cloud[ii].points[i][2])
                # int1.append(Cloud[ii].colors[i][0])


                x.extend(x1) # extend instead of append for this use case
                y.extend(y1)
                z.extend(z1)
                # intensity.extend(int1[i])
            X_ref.extend(x)
            Y_ref.extend(y)
            Z_ref.extend(z)
            # int_ref.extend(intensity)
            
            x = []
            y = []
            z = []
            # intensity = []
        X_ref_final.extend(X_ref)
        Y_ref_final.extend(Y_ref)
        Z_ref_final.extend(Z_ref)
        # int_ref_final.extend(int_ref)
        
        # disp(iii) % extraction progress meter 
        X_ref = []
        Y_ref = []
        Z_ref = []
        # int_ref = []

    ########################### Reconstruction of the point cloud ###########################
    #In MATLAB, the line ref = [X_ref_final; Y_ref_final; Z_ref_final]' is creating a matrix ref by vertically concatenating 
    # the vectors X_ref_final, Y_ref_final, and Z_ref_final, and then transposing the result. 
    # The resulting matrix will have each vector as a row.
    # This is how the line looks in matlab -- ref = [X_ref_final; Y_ref_final; Z_ref_final]'; 
    ref = np.array([X_ref_final, Y_ref_final, Z_ref_final]).T

    # PC_corr1 = pointCloud(ref,'Intensity',int_ref_final')

    # if gridStep == 0:
    #     PC_downsampled_1 = PC_corr1
    # else:
    #     PC_downsampled_1 = pcdownsample(PC_corr1,'gridAverage',gridStep)

    # # Remove invalid valuesbande_sep
    # [PC_Final1,indices]= removeInvalidPoints(PC_downsampled_1);

    # # Create the rotation matrix (velodyne)
    # RotX = [1 0 0 0; 0 cosd(-90) -sind(-90) 0; 0 sind(-90) cosd(-90) 0; 0 0 0 1];

    # # Apply the rotation to point cloud to align Z axis upwards (velodyne)
    # PC_Final1 = pctransform(PC_Final1, affine3d(RotX));

    # # Point cloud export with Seperate Filesand Merged Files (velodyne)
    # # In this part of the code, the scatterplot is exported. 

    # # Defining output document names
    # filename = sprintf('%s_%d.ply', output_file_name, iiii);

    # # Write file
    # pcloud{1,ii} = PC_Final1;
    # pcwrite(PC_Final1,filename,'PLYFormat','binary');

    # # Store filenames for later merging
    # filesToMerge{bande_sep} = fullfile(output, filename);
    # disp(['File stored for merging: ', filesToMerge{bande_sep}]);

    # ref = []; # suppression of the loaded point cloud
    # if puck == 1
    # f = msgbox((["Processed File:";output_file_name,'_', num2str(iiii) ' of 16\n']),"Status");
    # else
    # f = msgbox((["Processed File:";output_file_name,'_', num2str(iiii) ' of 32\n']),"Status");
    # end
    # pause(1)
    # if isvalid(f); delete(f); end
    # end