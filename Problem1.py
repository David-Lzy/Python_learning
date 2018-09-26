import copy
import math
import random
import sympy
import numpy
import xlrd



#X = 0
#Y = 0
#Z = 0
radar_number = 5
#single_radar_location = [0, 0, 0]
#all_radar_location = [single_radar_location for i in range(radar_number)]
all_radar_location = numpy.array([[80,0,0],[30,60,0],[55,110,0],[105,110,0],[130,60,0]])

time_list = 20
single_fake_track = [0, 0, 0]
all_fake_track = [single_fake_track for i in range(time_list)]
all_fake_track[0] = [60600,69982,7995]
all_fake_track[1] = [61197,69928,7980]
all_fake_track[2] = [61790,69838,7955]
all_fake_track[3] = [62377,69713,7920]
all_fake_track[4] = [62955,69553,7875]
all_fake_track[5] = [63523,69359,7820]
all_fake_track[6] = [64078,69131,7755]
all_fake_track[7] = [64618,68870,7680]
all_fake_track[8] = [65141,68577,7595]
all_fake_track[9] = [65646,68253,7500]
all_fake_track[10] = [66131,67900,7395]
all_fake_track[11] = [66594,67518,7280]
all_fake_track[12] = [67026,67116,7155]
all_fake_track[13] = [67426,66697,7020]
all_fake_track[14] = [67796,66263,6875]
all_fake_track[15] = [68134,65817,6720]
all_fake_track[16] = [68442,65361,6555]
all_fake_track[17] = [68719,64897,6380]
all_fake_track[18] = [68966,64429,6195]
all_fake_track[19] = [69184,63957,6000]

UAV_number = 60
A = 0  #X=At
B = 0  #Y=Bt
C = 0  #Z=Ct
#T = {'1': 0}
UAV_location = [0 for i in range(6)
                ]  #[X_0,Y_0,Z_0,A,B,C]identitfy a point when t identitfied
radar_to_fit = [[False for i in range(time_list)] for j in range(radar_number)]
#print(radar_to_fit[0])
single_UAV_information = [UAV_location, radar_to_fit]
all_UAV_information = [single_UAV_information for i in range(UAV_number)]

#print(all_UAV_information)
solution_number = 1
UAV_need_number = 0
single_solution = [all_UAV_information, UAV_need_number]
all_solution = [single_solution for i in range(solution_number)]


def delete_Duplicated_Element(listA):
    return sorted(set(listA), key=listA.index)


def check_if_problem_solved(single_solution):
    all_UAV_information = single_solution[0]
    UAV_need_number = single_solution[1]
    fit_situation = numpy.array(
        [(-1 for a in range(radar_number)) for b in range(time_list)])
    result = [True, fit_situation, time_list + 1]
    for j in range(time_list):
        radar_fited_number = 0
        for k in range(radar_number):
            #location = [False for n in range(radar_number)]
            for i in range(UAV_need_number):
                if all_UAV_information[i][1][j][k] == True:
                    fit_situation[j][k] = i
                    radar_fited_number = radar_fited_number + 1
                    #location[k] = True
        if radar_fited_number < 3:
            if result[0] == True:
                result[0] = False
                result[2] = j
    return result


def Reorganization(target_information, all_information):
    def fit_situation(single_information):
        single_fit_situation = numpy.array([])
        #print(single_information)
        for i_UAV in range(single_information[0][1]):
            radar_to_fit = single_information[0][0][i_UAV][1]
            cover_number = 0
            for a in radar_to_fit:
                for b in radar_to_fit[a]:
                    if radar_to_fit[a][b] == True:
                        cover_number = cover_number + 1
            single_fit_situation = numpy.append([i_UAV, cover_number],
                                                single_fit_situation)
        return single_fit_situation

    Reorganization_time = 20
    Reorganization_ID = []
    #dlete_number = []
    #radar_to_fit = target_information[0][0][i][1]
    target_fit_situation = fit_situation(target_information)
    for i in range(Reorganization_time):
        this_ID = random.randint(0, len(all_information))
        if this_ID in Reorganization_ID:
            this_ID = random.randint(0, len(all_information))
    for i in Reorganization_ID:
        be_fitted_situation = fit_situation(all_information[i])
        if min(target_fit_situation[:, 1]) >= max(be_fitted_situation[:, 1]):
            if random.random(0, 2) >= 1:
                #dlete_number = numpy.append(i, dlete_number)
                #del all_information[i]
                all_information[i] = target_information
        else:
            #be_fitted_radar_to_fit = all_information[i][0][0][i][1]
            #1、如果A第i个无人机所对应的轨道在B上空，复制
            #2、如果A第i个无人机所对应的轨道在B上有被占，但是那两个占的轨道都没自己好，
            #   all_information扩增占(记得删除旧轨道)或者没占
            for i_UAV in range(target_information[0][1]):
                target_radar_to_fit = target_information[0][0][i_UAV][1]
                for j_UAV in range(all_information[i][0][1]):
                    be_fitted_radar_to_fit = all_information[i][0][0][j_UAV][1]
                    similiar_strength = 0
                    target_fit_number = 0
                    be_fitted_fit_number = 0
                    ready_to_cover = 0
                    whose_will_cover = []
                    for a in range(len(target_radar_to_fit)):
                        for b in range(len(target_radar_to_fit[a])):
                            if target_radar_to_fit[a][b] == True:
                                target_fit_number = target_fit_number + 1
                                if target_information[1][1][b][a] == -1:
                                    ready_to_cover = ready_to_cover + 1
                                else:
                                    if target_information[1][1][b][
                                            a] in whose_will_cover:
                                        pass
                                    else:
                                        whose_will_cover = numpy.append(
                                            target_information[1][1][b][a],
                                            whose_will_cover)
                            if be_fitted_radar_to_fit[a][b] == True:
                                be_fitted_fit_number = be_fitted_fit_number + 1
                            if (target_radar_to_fit[a][b] ==
                                    be_fitted_radar_to_fit[a][b]):
                                similiar_strength = similiar_strength + 1
                    if ready_to_cover == target_fit_number:
                        all_information[i][0][1] = all_information[i][0][1] + 1
                        all_information[i][0][0][all_information[i][0][
                            1]] = target_information[0][0][i_UAV]
                    else:
                        dont_cover = []
                        for i_will_be_covered in whose_will_cover:
                            i_dont_cover = 0
                            for a in all_information[i][0][0][
                                    i_will_be_covered][1]:
                                for b in all_information[i][0][0][
                                        i_will_be_covered][1][a]:
                                    if all_information[i][0][0][
                                            i_will_be_covered][1][a] == True:
                                        i_dont_cover = i_dont_cover + 1
                            dont_cover = numpy.append(i_dont_cover, dont_cover)
                        if target_fit_number >= max(dont_cover):
                            if random.random > 0.4:
                                whose_will_cover = whose_will_cover[
                                    numpy.argsort(whose_will_cover)][::-1]
                                for i_will_be_covered in range(
                                        len(whose_will_cover)):
                                    del (all_information[i][0][0][
                                        i_will_be_covered])
                                    all_information[i][0][
                                        1] = all_information[i][0][1] - 1
                                all_information[i][0][
                                    1] = all_information[i][0][1] + 1
                                all_information[i][0][0][all_information[i][0][
                                    1]] = target_information[0][0][i_UAV]
                            else:
                                pass
    return all_information


uselsess_Permutations = []  # 任取三个点，结果这三个点任取两个都不行2333

#[(0 for a in range(radar_number)) for b in range(time_list)]


def mutation(target_information, uselsess_Permutations):
    #突变
    def if_picked_points_fit_real(i_Permutation, uselsess_Permutations):#部分林炜的程序整合
        radar = numpy.array([[80,0,0],[30,60,0],[55,110,0],[105,110,0],[130,60,0]])
        fake = numpy.loadtxt('fake_track.dat')/1000 #unit km
        x0, y0, z0, vx, vy, vz = sympy.symbols('x0 y0 z0 vx vy vz') #velocity km/h
        def lines_solve(f0,radar0,fake0,f1,radar1,fake1,f2,radar2,fake2):#穿过三个线的解
            #first radar x0 = radar[0] y0 = radar[1]  z0 = radar[2]
            t0,t1,t2 = f0/360, f1/360, f2/360 # unit to h
            #print(radar2,fake2)
            result = sympy.solve([
                        (x0+vx*t0-radar0[0])*(fake0[1]-radar0[1])-(y0+vy*t0-radar0[1])*(fake0[0]-radar0[0]),
                        (y0+vy*t0-radar0[1])*(fake0[2]-radar0[2])-(z0+vz*t0-radar0[2])*(fake0[1]-radar0[1]),
                        (x0+vx*t1-radar1[0])*(fake1[1]-radar1[1])-(y0+vy*t1-radar1[1])*(fake1[0]-radar1[0]),
                        (y0+vy*t1-radar1[1])*(fake1[2]-radar1[2])-(z0+vz*t2-radar1[2])*(fake1[1]-radar1[1]),
                        (x0+vx*t2-radar2[0])*(fake2[1]-radar2[1])-(y0+vy*t2-radar2[1])*(fake2[0]-radar2[0]),
                        (y0+vy*t2-radar2[1])*(fake2[2]-radar2[2])-(z0+vz*t2-radar2[2])*(fake2[1]-radar2[1])
                        ],
                        [x0, y0, z0, vx, vy, vz] , dict=True)
            return result

        def get_points(result):#获取解之后判断是否满足题目要求
            points = {'check':False,'radar_frame':numpy.zeros([20,5],dtype ='bool_'),'xyz':[]}#[20,5]<-[5,20]
            if result:
                V = result[0][vx]**2+result[0][vy]**2+result[0][vz]**2
                if 14400<=V<=32400:
                    for iframe in range(20):
                        t_h = iframe/360.0
                        for iradar in range(5):
                            z_real = result[0][z0]+result[0][vz]*t_h
                            #print(z_real)
                            if 2<=z_real<=2.5:
                                x_real = result[0][x0]+result[0][vx]*t_h
                                y_real = result[0][y0]+result[0][vy]*t_h
                                if (abs((x_real-radar[iradar][0])*(fake[iframe][1]-radar[iradar][1])
                                /((y_real-radar[iradar][1])*(fake[iframe][0]-radar[iradar][0]))-1)<0.01 and
                                abs((x_real-radar[iradar][0])*(fake[iframe][2]-radar[iradar][2])
                                /((z_real-radar[iradar][2])*(fake[iframe][0]-radar[iradar][0]))-1)<0.01):
                                    points['radar_frame'][iframe,iradar] = True#[20,5]<-[5,20]
                        if numpy.sum(points['radar_frame'])>=2:
                            points['check']=True
                            points['xyz']=result[0]
            return points

        def two_points_solve(f0,radar0,fake0,f1,radar1,fake1):
            t0, t1 = f0 / 360, f1 / 360
            picked_time_list = [t0, t1]
            z_real_limits = [2, 2.5]
            all_rader = [radar0,radar1]
            all_fake = [fake0,fake1]
            v_collection = numpy.zeros([len(z_real_limits)*len(z_real_limits)])
            #v_collection = numpy.zeros([2])
            calculated_points = numpy.zeros([2,2,3])#time_list、z、dimension
            for k_time in range(len(picked_time_list)):
                for j_limit in range(len(z_real_limits)):
                    ratio = (z_real_limits[j_limit] - all_rader[k_time][2]) / (
                        all_fake[k_time][2] - all_rader[k_time][2])
                    calculated_points[
                        k_time, j_limit, 0] = all_rader[k_time][0] * (
                            1 - ratio) + all_fake[k_time][0] * ratio
                    calculated_points[
                        k_time, j_limit, 1] = all_rader[k_time][1] * (
                            1 - ratio) + all_fake[k_time][1] * ratio
                    calculated_points[k_time, j_limit, 2] = j_limit
            for i_limit in range(len(z_real_limits)):
                for j_limit in range(len(z_real_limits)):
                    for i_dimension in range(3):
                        i = k_time * len(z_real_limits) + j_limit
                        v_collection[i] = v_collection[i] + (calculated_points[1,i_limit,i_dimension] - calculated_points[0,j_limit,i_dimension]) ** 2
            if max(v_collection) < 14400:
                if min(v_collection) > 32400:
                    return False
            else:
                return True

        def pick_two_points_frome_three(i_Permutation):
            j_i_Permutation = []
            for i in range(len(i_Permutation)):
                for j in range(len(i_Permutation)-1):
                    if j < i:
                        j_i_Permutation = numpy.append(i_Permutation[j],j_i_Permutation)
                    else:
                        j_i_Permutation = numpy.append(i_Permutation[j+1],j_i_Permutation)
            picked = random.randint(0, len(j_i_Permutation))
            return picked
        if len(i_Permutation) == 3:
            if i_Permutation in uselsess_Permutations:
                j_i_Permutation = pick_two_points_frome_three(i_Permutation)
                if_picked_points_fit_real(j_i_Permutation, uselsess_Permutations)
            else:
                function = lines_solve(i_Permutation[0][0],i_Permutation[0][1][0],all_fake_track(i_Permutation[0][0]),
                    i_Permutation[1][0],i_Permutation[0][1][0],all_fake_track(i_Permutation[1][0]),
                    i_Permutation[2][0],i_Permutation[0][1][0],all_fake_track(i_Permutation[2][0]))
                result_by_linwei = get_points(function)
                if result_by_linwei['check'] == False:
                    uselsess_Permutations = numpy.append(i_Permutation,uselsess_Permutations)
                    j_i_Permutation = pick_two_points_frome_three(i_Permutation)
                    if_picked_points_fit_real(j_i_Permutation, uselsess_Permutations)
                else:
                    single_UAV_information = [result_by_linwei['xyz'],result_by_linwei['radar_frame']]
                    return single_UAV_information
        elif len(i_Permutation) == 2:
            result2 = two_points_solve(
                i_Permutation[0][0],
                i_Permutation[0][1][0],
                all_fake_track(i_Permutation[0][0]),
                i_Permutation[1][0],
                i_Permutation[0][1][0],
                all_fake_track(i_Permutation[1][0]),
            )
            if result2 == True:
                #single_UAV_information = [UAV_location, radar_to_fit]
                i_radar_to_fit = [[False for i in range(time_list)]for j in range(radar_number)]
                for i_time_list in i_Permutation:
                    for j_radar in i_time_list[1]:
                        i_radar_to_fit[i_time_list[0]][j_radar] = True
                single_UAV_information = [[0,0,0,0,0,0],[i_radar_to_fit]]
                return single_UAV_information
            else:
                i_radar_to_fit = [[False for i in range(time_list)]for j in range(radar_number)]
                UAV_informations = []
                for i_time_list in i_Permutation:
                    for j_radar in i_time_list[1]:
                        i_radar_to_fit[i_time_list[0]][j_radar] = True
                        UAV_informations = numpy.append(
                            [[0, 0, 0, 0, 0, 0], [i_radar_to_fit]],
                            UAV_informations)
                single_UAV_information = UAV_informations[random.randint(0, len(UAV_informations))]
                return single_UAV_information

    def Traversing(unfitted_for_permutate):
        UAV_informations = []
        #for a in unfitted_for_permutate:
        #   for b in a[1]:
        #        pass
        All_Permutations = []
        temp = []
        for i in range(len(unfitted_for_permutate)):#遍历所有可能
            #this_picked_timelist_number = len(All_Permutations)
            for j in range(len(unfitted_for_permutate[i][1])):
                for k in range(len(All_Permutations)):
                    this_picking_radar = [
                        unfitted_for_permutate[i][0],
                        unfitted_for_permutate[i][i][j]
                    ]
                    temp = numpy.append(this_picking_radar,
                                        All_Permutations[k])
            All_Permutations = numpy.append(temp,All_Permutations)
        for i_Permutation in All_Permutations:
            UAV_informations = numpy.append(
                if_picked_points_fit_real(
                    i_Permutation, uselsess_Permutations), UAV_informations)
        cover_number = numpy.zeros([len(UAV_informations)])
        for i in range(len(UAV_informations)):
            for a in UAV_informations[i][1]:
                for b in a:
                    if b == True:
                        cover_number[i] = cover_number[i] + 1
        this_list = (numpy.where(UAV_informations == max(UAV_informations)))[0][0]
        single_UAV_information = UAV_informations[this_list]
        #this_list = this_list.tolist()
        #which_to_pick = random.randint(0, len(lit[0[0]]))
        return single_UAV_information

    def random_pick(unfitted_for_permutate):
        new_list = []
        for i in range(len(random_time_list)):
            random_time_list[i] = random.randint(
                0,
                len(unfitted_for_permutate) - i)
        for i in range(len(random_time_list) - 1):
            if random_time_list[i] <= random_time_list[i + 1]:
                for j in range(len(random_time_list) - i - 1):
                    random_time_list[i + j +
                                     1] = random_time_list[i + j + 1] + 1
        for i in range(len(random_time_list)):
            random_time_list[i] = unfitted_for_permutate[random_time_list[i]]
        for i in random_time_list:
            random_radar_list[i] = random.randint(
                0, len(unfitted_for_permutate[i]))
        for i in range(len(random_time_list)):
            new_list = numpy.append(
                [random_time_list[i], [random_radar_list[i]]], new_list)
        #稍后加上判断是否可行
        single_UAV_information =  if_picked_points_fit_real(new_list, uselsess_Permutations)
        return single_UAV_information#还是只返回一个解比较easy

    random_time_list = [0, 0, 0]
    random_radar_list = [0, 0, 0]
    unfitted_time = target_information[1][2]
    unfitted_for_permutate = numpy.array([])
    unfitted_number = 0
    #picked_points_list = []
    for a in range(unfitted_time, time_list):  #从没有完成的第一个时刻开始到最终时刻
        this_time_list_unfitted = []
        for b in range(target_information[1][1][a]):
            if target_information[1][1][a][b] == -1:
                this_time_list_unfitted = numpy.append(
                    b, this_time_list_unfitted)
                unfitted_number = unfitted_number + 1
        if len(this_time_list_unfitted) >= 3:
            unfitted_for_permutate.numpy.append([a, this_time_list_unfitted])
    if unfitted_number >= 5:
        if len(unfitted_for_permutate) >= 3:
            single_UAV_information = random_pick(unfitted_for_permutate)
        else:
            single_UAV_information = Traversing(unfitted_for_permutate)
            #最糟糕的是全部一个个点，不能是none
    target_information[0][1] = target_information[0][1] + 1
    target_information[0][0][target_information[0][1] +
                             1] = single_UAV_information
    return target_information


def evolution_of_solution(old_all_information,
                          uselsess_Permutations):  #这是一个突变或者重组的过程
    evolution_time = 100
    new_all_sloution = []
    #old_solution 即为all_solution中的某个all_UAV_information
    #old_solution无需删除，它自然会因为劣势而被清洗
    new_all_information = old_all_information
    print(new_all_information)
    if len(old_all_information) <= 10:
        for i_information in old_all_information:
            #突变
            j = 0
            while j <= evolution_time:
                if random.randint(0, 50) <= 40:
                    new_all_information = numpy.append(
                        mutation(i_information, uselsess_Permutations),new_all_information)
                j = j + 1
    else:
        for i_information in old_all_information:
            #突变或者重组
            j = 0
            while j <= evolution_time:
                if random.randint(0, 50) <= 10:
                    new_all_information = numpy.append(
                        mutation(i_information, uselsess_Permutations),new_all_information)
                elif random.randint(0, 50) >= 20:
                    print(i_information)
                    new_all_information = new_all_information + Reorganization(
                        i_information, old_all_information)

                j = j + 1
    delete_Duplicated_Element(new_all_information)
    for i in new_all_information:
        new_all_sloution = numpy.append(new_all_information[i][0],
                                        new_all_sloution)
    delete_Duplicated_Element(new_all_sloution)
    return new_all_sloution


#all_UAV_information = [single_UAV_information for i in range(UAV_number)]
#single_solution = [all_UAV_information, UAV_need_number]
#all_solution = [single_solution for i in range(solution_number)]
#result = [True, fit_situation, time_list + 1]
#fit_situation = [(0 for a in range(radar_number))for b in range(time_list)]


#single_information = [i_solution,result]
def Pick_better_solutions(all_information):  #kill
    solution_number = len(all_information)
    how_many_to_pick = 1000
    if solution_number <= how_many_to_pick:
        return all_information
    else:
        pick_ratio = (1 - how_many_to_pick / solution_number) * 0.5
        all_radar_fit = []
        all_UAV_number = []
        all_fit_ratio = []
        new_all_information = []
        for single_information in all_information:
            this_radar_fit = 0
            this_UAV_number = single_information[0][0][1]
            all_UAV_number = numpy.append(this_UAV_number, all_UAV_number)
            for a in range(radar_number):
                for b in range(time_list):
                    if single_information[1][1][b][a] >= 0:
                        this_radar_fit = this_radar_fit + 1
            all_radar_fit = numpy.append(this_radar_fit, all_radar_fit)
            try:
                fit_ratio = this_radar_fit / this_UAV_number
            except Exception:
                fit_ratio = 1  #一个无人机一个坑，最辣鸡的解了
            finally:
                all_fit_ratio = numpy.append(fit_ratio, all_fit_ratio)
        max_radar_fit = max(all_radar_fit)
        min_radar_fit = min(all_radar_fit)
        valueable_fit = pick_ratio * max_radar_fit + (
            1 - pick_ratio) * min_radar_fit
        min_fit_ratio = min(all_fit_ratio)
        for i in range(len(all_information)):
            if all_radar_fit[i] >= valueable_fit:
                if all_fit_ratio[i] > min_fit_ratio:
                    new_all_information = numpy.append(all_information[i],
                                                       new_all_information)
        Pick_better_solutions(new_all_information)

    #old_all_solution


UAV_need_number = 0
unfitted_time = 0
good_result_number = 0
#single_information = [i_solution,result]
while True:

    all_information = []

    for i_solution in all_solution:
        result = check_if_problem_solved(i_solution)
        single_information = [i_solution, result]
        all_information = numpy.append(single_information, all_information)
        if result[0] == True:
            print('有一个极优解最终活了下来')
            good_result_number = good_result_number + 1
            print(i_solution)
        if good_result_number >= 2:
            break

    all_information = Pick_better_solutions(all_information)

    #all_solution = []
    #for single_information in all_information:
    #   #print(single_information[0])
    #    all_solution = numpy.append(single_information[0], all_solution)

    evolution_of_solution(all_information, uselsess_Permutations)
