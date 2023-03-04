import json
import pandas as pd

#%% Create dataframe

def create_dataframe(account_data_list):
  # create empty dataframe
  dataframe = pd.DataFrame({})
  
  # loop to rename all fields according to variable naming
  for account_data in account_data_list:
    user_follower_count = account_data["userFollowerCount"]
    user_following_count = account_data["userFollowingCount"]
    follower_following_ratio = user_follower_count/max(1,user_following_count)
    
    temp_dataframe = pd.Series({"user_media_count":account_data["userMediaCount"],
                                "user_follower_count":account_data["userFollowerCount"],
                                "user_following_count":account_data["userFollowingCount"],
                                "user_has_profil_pic":account_data["userHasProfilPic"],
                                "user_is_private":account_data["userIsPrivate"],
                                "follower_following_ratio":follower_following_ratio,
                                "user_biography_length":account_data["userBiographyLength"],
                                "username_length":account_data["usernameLength"],
                                "username_digit_count":account_data["usernameDigitCount"],
                                  "is_fake":account_data["isFake"]
                                })
                            
    dataframe = pd.concat([dataframe, temp_dataframe], ignore_index=True, axis=1)
  return dataframe # return as dataframe

#%% Import automated/nonautomated data
		
def import_data(dataset_path, dataset_version):

  # open dataset
  with open(dataset_path + "/" + dataset_version + "/fakeAccountData.json") as json_file:
      fake_account_data = json.load(json_file)
  with open(dataset_path + "/" + dataset_version + "/realAccountData.json") as json_file:
      real_account_data = json.load(json_file)
      
  # create dataframe
  fake_account_dataframe = create_dataframe(fake_account_data)
  real_account_dataframe = create_dataframe(real_account_data)
  merged_dataframe = pd.concat([fake_account_dataframe, real_account_dataframe], 
                               ignore_index=True, axis=1)
  data = dict({"dataset_type":"fake/real",
                  "dataframe":merged_dataframe})
      
  # return data # return as dictionaries
  return merged_dataframe # return as dataframe
