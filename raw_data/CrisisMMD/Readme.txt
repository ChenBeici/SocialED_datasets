CrisisMMD version 2.0

﻿Description of the dataset
==========================
The CrisisMMD multimodal Twitter dataset consists of several thousands of manually annotated tweets and images collected during seven major natural disasters including earthquakes, hurricanes, wildfires, and floods that happened in the year 2017 across different parts of the World. The provided datasets include three types of annotations (for details please refer to our paper [1] and [2]):

Change log v2.0: In this version of this dataset, we mapped "Not relevant or can't judge" to "Not humanitarian" for the humanitarian task. Also the "Not informative" label from informative task also mapped to "Not humanitarian" for the humanitarian task. We also removed duplicate entries that appeared while combined the tweets from different events. Both informative and humanitarian tasks are now aligned and can be useful for multitask classification learning. 

** Task 1: Informative vs Not informative
   * Informative
   * Not informative
** Task 2: Humanitarian categories
   * Affected individuals
   * Infrastructure and utility damage
   * Injured or dead people
   * Missing or found people
   * Rescue, volunteering or donation effort
   * Vehicle damage
   * Other relevant information
   * Not humanitarian
** Task 3: Damage severity assessment
   * Severe damage
   * Mild damage
   * Little or no damage


Data format and directories
===========================
The data directory contains the following three sub-directories:

1. "annotations": This directory contains seven tab-separated values (i.e., TSV) files, one for each disaster event in our dataset. Each TSV file stores ground-truth annotations for the aforementioned humanitarian tasks. The data format of these files is described in detail below.

2. "data_image": This directory contains all the images (in JPG format) in our dataset, organized into the following folder structure. There are seven folders with disaster event names. Each event folder consists of several subfolders corresponding to different days of the event, and each subfolder contains all the images collected for the event on that day.

3. "json": This directory contains seven JSON files representing seven disaster events. Each file contains all the raw data obtained from Twitter for each disaster event. Each line in a file corresponds to data from a single tweet stored in JSON format (as downloaded from Twitter).

4. "crisismmd_datasplit_all.zip" - Training, development and test set split.

Format of the TSV files under the "annotations" directory
---------------------------------------------------------
Each TSV file in this directory contains the following columns, separated by a tab:

* tweet_id: corresponds to the actual tweet id from Twitter.
* image_id: corresponds to a combination of a "tweet_id" and an index concatenated with an underscore. The integer indices represent different images associated with a given tweet.
* text_info: corresponds to the informative label (i.e., informative, not_informative, dont_know_or_cant_judge) assigned to a given tweet text.
* text_info_conf: corresponds to the confidence score associated with the "text_info" label (provided by Figure Eight (https://www.figure-eight.com/), previously known as CrowdFlower) of a given tweet text.
* image_info: corresponds to the informative label (i.e., informative, not_informative, dont_know_or_cant_judge) assigned to a given tweet image.
* image_info_conf: corresponds to the confidence score associated with the "image_info" label (provided by Figure Eight (https://www.figure-eight.com/), previously known as CrowdFlower) of a given tweet image.
* text_human: corresponds to the humanitarian label (see the list of humanitarian task labels above) assigned to a given tweet text.
* text_human_conf: corresponds to the confidence score associated with the "text_human" label (provided by Figure Eight (https://www.figure-eight.com/), previously known as CrowdFlower) of a given tweet text.
* image_human: corresponds to the humanitarian label (see the list of humanitarian task labels above) assigned to a given tweet image.
* image_human_conf: corresponds to the confidence score associated with the "image_human" label (provided by Figure Eight (https://www.figure-eight.com/), previously known as CrowdFlower) of a given tweet image.
* image_damage: corresponds to the damage severity assessment label (see the list of damage severity assessment task labels above) assigned to a given tweet image.
* image_damage_conf: corresponds to the confidence score associated with the "image_damage" label (provided by Figure Eight (https://www.figure-eight.com/), previously known as CrowdFlower) of a given tweet image.
* tweet_text: corresponds to the original text of a given tweet as downloaded from Twitter.
* image_url: corresponds to the original image URL of a given tweet provided by Twitter.
* image_path: corresponds to the relative path of an image inside the "data_image" folder for a given tweet.

Note that there are empty (i.e., null) entries in the TSV files that simply indicate "not applicable" cases. For example, for a given pair of tweet text and image, if neither the text nor the image is labeled as informative (i.e., text_info != informative & image_info != informative), then the given tweet text/image pair is excluded from the rest of the annotation tasks (i.e., humanitarian and damage severity assessment tasks). Similarly, for the damage severity assessment task, we included only the subset of images that were labeled as "infrastructure and utility damage" and excluded all other images from the task. In such cases, we have empty (i.e., null) entries in our annotation tables.


Author name and affiliation
===========================
* Firoj Alam (Qatar Computing Research Institute, Hamad Bin Khalifa University)
ORCID: 0000-0001-7172-1997

* Ferda Ofli (Qatar Computing Research Institute, Hamad Bin Khalifa University)
ORCID: 0000-0003-3918-3230

* Muhammad Imran (Qatar Computing Research Institute, Hamad Bin Khalifa University)
ORCID: 0000-0001-7882-5502

For issues and inquiries, please contact:
Ferda Ofli (fofli@hbku.edu.qa)
Muhammad Imran (mimran@hbku.edu.qa)


Citation
========
If you use this data in your research, please consider citing the following papers:

[1] Ferda Ofli, Firoj Alam and Muhammad Imran. Analysis of Social Media Data using Multimodal Deep Learning for Disaster Response. 17th International Conference on Information Systems for Crisis Response and Management (ISCRAM), 2020, Blacksburg, Virginia, USA.
[2] Firoj Alam, Ferda Ofli and Muhammad Imran. CrisisMMD: Multimodal Twitter Datasets from Natural Disasters. International AAAI Conference on Web and Social Media (ICWSM), 2018, Stanford, California, USA.


@inproceedings{multimodalbaseline2020,
Author = {Ferda Ofli and Firoj Alam and Muhammad Imran},
Booktitle = {17th International Conference on Information Systems for Crisis Response and Management},
Keywords = {Multimodal deep learning, Multimedia content, Natural disasters, Crisis Computing, Social media},
Month = {May},
Organization = {ISCRAM},
Publisher = {ISCRAM},
Title = {Analysis of Social Media Data using Multimodal Deep Learning for Disaster Response},
Year = {2020}

}
@inproceedings{CrisisMMD2018,
	Address = {Stanford, California, USA},
	Author = {Firoj Alam and Ferda Ofli and Muhammad Imran},
	Booktitle = {AAAI Conference on Web and Social Media (ICWSM)},
	Keywords = {Multimodal, Twitter datasets, Textual and multimedia content, Natural disasters},
	Month = {June},
	Organization = {AAAI},
	Publisher = {AAAI},
	Title = {CrisisMMD: Multimodal Twitter Datasets from Natural Disasters},
	Year = {2018}
}

Terms of Use
============
Please follow the terms of use mentioned here:
https://dataverse.mpi-sws.org/dataset.xhtml?persistentId=doi%3A10.5072%2FFK2%2F0YU5RD
