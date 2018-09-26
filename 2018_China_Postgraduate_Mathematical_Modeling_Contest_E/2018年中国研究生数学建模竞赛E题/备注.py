UAV_need_number = 0
solution_number = 0
radar_number = 5
single_radar_location = [0, 0, 0]
all_radar_location = [single_radar_location for i in range(radar_number)]

time_list = 20
single_fake_track = [0, 0, 0]
all_fake_track = [single_fake_track for i in range(time_list)]

UAV_number = 60
A = 0  #X=At
B = 0  #Y=Bt
C = 0  #Z=Ct
T = {'1': 0}
UAV_location = [0 for i in range(6)
                ]  #[A,B,C,X_0,Y_0,Z_0]identitfy a point when t identitfied
#UAV_location = single_UAV_information[0]
#UAV_location = all_UAV_information[i][0]
#UAV_location = single_solution[0][i][0]
#UAV_location = single_information[0][0][i][0]

radar_to_fit = [[False for i in range(time_list)] for j in range(radar_number)]
#radar_to_fit = single_UAV_information[1]
#radar_to_fit = all_UAV_information[i][1]
#radar_to_fit = single_solution[0][i][1]
#radar_to_fit = single_information[0][0][i][1]

single_UAV_information = [UAV_location, radar_to_fit]
#single_UAV_information = all_UAV_information[i]

all_UAV_information = [single_UAV_information for i in range(UAV_number)]
#all_UAV_information = single_solution[0]
#all_UAV_information = single_information[0][0]

single_solution = [all_UAV_information, UAV_need_number]
#single_solution = single_information[0]

all_solution = [single_solution for i in range(solution_number)]

fit_situation = [(0 for a in range(radar_number)) for b in range(time_list)]
#填坑情况[第b时间段][第a个坑] = 被第几个无人机填了
#fit_situation = result[1]
#fit_situation = single_information[1][1]

result = [True, fit_situation, time_list + 1]
#result = single_information[1]

single_information = [single_solution, result]
#是否解决问题，填坑情况，在第几步不符合条件