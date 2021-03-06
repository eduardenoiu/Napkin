
import pandas as pd

# TODO: This file should be replaced by a session configuration file that is dynamically composed by a
#      session handler tool!


# EXAMPLE:
# for name,grp in req_tc_map.groupby('TC'):   #or ('REQ')
#    print (name)
#    print (grp['REQ'].values)
#    print ("--------------------------------------------------------------")
#
#print ( "==============================================================")
#print ("==============================================================")
# for name,grp in req_tc_map.groupby('REQ'):
#    print (name)
#    print (grp['TC'].values)
#    print ("--------------------------------------------------------------")
#

req_info = [  # pd.DataFrame(\
    {'REQ': 'SR_C30_SRS_Safe-REQ-349', 'TC': 'TC-DriveBrake-S-013',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-349'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-260', 'TC': 'TC-DriveBrake-S-011',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-260'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-248', 'TC': 'TC-DriveBrake-S-018',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-248'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-258', 'TC': 'TC-DriveBrake-S-001',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-258'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-259', 'TC': 'TC-DriveBrake-S-001',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-259'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-281', 'TC': 'TC-DriveBrake-S-021',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-281'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-283', 'TC': 'TC-DriveBrake-S-019',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-283'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-254', 'TC': 'TC-DriveBrake-S-005',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-254'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-255', 'TC': 'TC-DriveBrake-S-007',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-255'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-245', 'TC': 'TC-DriveBrake-S-016',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-245'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-244', 'TC': 'TC-DriveBrake-S-016',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-244'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-244', 'TC': 'TC-DriveBrake-S-024',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-244'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-456', 'TC': 'TC-DriveBrake-S-068',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-456-A1'}, {'name': 'SR_C30_SRS_Safe-REQ-456-A2'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-246', 'TC': 'TC-DriveBrake-S-017',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-246'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-253', 'TC': 'TC-DriveBrake-S-003',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-253'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-290', 'TC': 'TC-DriveBrake-S-020',
        'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-290'}]},
    {'REQ': 'SR_C30_SRS_Safe-REQ-350', 'TC': 'TC-DriveBrake-S-007', 'ga_list': [{'name': 'SR_C30_SRS_Safe-REQ-350'}]}]


req_tc_map = pd.DataFrame(req_info)


def _create_traceability_map(req_info):
    tcmap = {}
    tcmaplist = pd.DataFrame(req_info)
    for _ix, row in tcmaplist.iterrows():
        tc = row['TC']
        rq = row['REQ']
        rqs = tcmap.get(tc, [])
        rqs.append(rq)
        tcmap[tc] = rqs
    return tcmap


traceability_map = _create_traceability_map(
    req_info)  # This is how its constructed

tc_filename_map = {
    '001': 'TC-DriveBrake-S-001.xml',
    '003': 'TC-DriveBrake-S-003.xml',
    '005': 'TC-DriveBrake-S-005.xml',
    '007': 'TC-DriveBrake-S-007.xml',
    '011': 'TC-DriveBrake-S-011.xml',
    '013': 'TC-DriveBrake-S-013.xml',
    '016': 'TC-DriveBrake-S-016.xml',
    '017': 'TC-DriveBrake-S-017.xml',
    '018': 'TC-DriveBrake-S-018.xml',
    '019': 'TC-DriveBrake-S-019.xml',
    '020': 'TC-DriveBrake-S-020.xml',
    '021': 'TC-DriveBrake-S-021.xml',
    '024': 'TC-DriveBrake-S-024.xml',
    '068': 'TC-DriveBrake-S-068.xml',
    '099': '1.0.95 Route Cycle A1.xml'
}


def mandatory_req(req, tc):
    '''
    Checks if the requirement is mandatory for the given test case     


    Parameters
    ----------
    req : string e.g 'SR_C30_SRS_Safe-REQ-350'

    tc : string e.g. 'TC-DriveBrake-S-007'


    Returns
    -------
    Bool
         True if mandatory, False if optional

    '''
    reqs = traceability_map[tc]
    return req in reqs


tc_log_steps = {'TC-DriveBrake-S-001': '5:15',
                'TC-DriveBrake-S-003': '7:14',
                'TC-DriveBrake-S-005': '2:11',
                'TC-DriveBrake-S-007': '5:23',
                'TC-DriveBrake-S-011': '6:59',
                'TC-DriveBrake-S-013': '2:11',
                'TC-DriveBrake-S-016': '5:18',
                'TC-DriveBrake-S-017': '3:15',
                'TC-DriveBrake-S-018': '3:14',
                'TC-DriveBrake-S-019': '7:15',
                'TC-DriveBrake-S-020': '6:11',
                'TC-DriveBrake-S-021': '1:26',
                'TC-DriveBrake-S-024': '3:12',
                'TC-DriveBrake-S-068': '7:13'}

test_case_list = list(tc_log_steps.keys())
