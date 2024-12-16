================
Data description
================
This datasets consist of tweets collected during the 2015 Nepal Earthquake and the 2013 Queensland Flood. The annotation of relevant and irrelevant (not_relevant) categories consist of 11,668 tweets for the Nepal Earthquake dataset and 10,033 tweets for the Queensland dataset.

For each dataset, we also release ids of the tweets of the unlabelled data that we used for our experiments. One can use our Tweet retrieval tool (available on CrisisNLP.qcri.org) to download the tweets based on ids provided in the datasets.

============
Data formats
============
Each .tsv file contains 3 columns separated by tab: 1) id, 2) text of the tweet, and 3) class label. The .txt file contains tweets ids, which are not labeled. 

2015 Nepal Earthquake:
--------------
nepal/2015_Nepal_Earthquake_train.tsv -- 7000 labeled tweets
nepal/2015_Nepal_Earthquake_dev.tsv  -- 1166 labeled tweets
nepal/2015_Nepal_Earthquake_test.tsv  -- 3502 labeled tweets
nepal/2015_Nepal_Earthquake_unlabelled_ids.txt -- 864,966 un-labeled tweet ids


2013 Queensland Flood:
---------------
queensland/2013_Queensland_Floods_train.tsv -- 6019 labeled tweets 
queensland/2013_Queensland_Floods_dev.tsv -- 1003 labeled tweets 
queensland/2013_Queensland_Floods_test.tsv -- 3011 labeled tweets
queensland/2013_Queensland_Floods_unlabelled_ids.txt -- 21,917  un-labeled tweet ids


====================
Citation information
====================

If you this data in your research, please cite one of the following papers:

Firoj Alam, Shafiq Joty, Muhammad Imran. Domain Adaptation with Adversarial Training and Graph Embeddings. In proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL), 2018, Melbourne, Australia. 

Firoj Alam, Shafiq Joty, Muhammad Imran. Graph Based Semi-supervised Learning with Convolutional Neural Networks to Classify Crisis Related Tweets, International AAAI Conference on Web and Social Media (ICWSM), 2018, Stanford, California, USA.


============
Terms of Use
============
THE DATA IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
By downloading or using any of the material available on this site, you automatically acknowledge to the following conditions:
By way of example and not as a limitation, when using these materials, you shall not do any of the following: 
- Defame, abuse, harass, stalk, threaten or otherwise violate the legal rights (such as rights of privacy and publicity) of others; 
- Publish, post, distribute or disseminate any defamatory, infringing, obscene, indecent or unlawful material or information;
You will be liable for any loss or damage in connection with this data 
IN NO EVENT SHALL QCRI OR QCRI’s AFFILIATES BE LIABLE TO THE REQUESTER OR TO THE USER OF THE DATA SUPPLIED FOR ANY SPECIAL, INCIDENTAL, PUNITIVE, INDIRECT, EXEMPLARY, OR CONSEQUENTIAL DAMAGES.THIS DATA IS PROVIDED ON AN “AS IS” BASIS AND YOUR USE OF IT IS AT YOUR SOLE RISK.YOU WILL INDEMNIFY QCRI OR QCRI's AFFILIATES FOR ANY LOSS OR DAMAGE THEY MAY SUFFER ARISING OF ANY BREACH BY YOU OF THIS AGREEMENT.
- You will use the data only for research on humanitarian computing.
- You will keep the contents of these dataset(s) confidential (you can always share the tweet-ids).
- The dataset(s) will be deleted by you upon our request at any time (you can always keep the tweet-ids).
- The dataset(s) will be deleted by you upon completion of the research (you can always keep the tweet-ids).
- You will cite the corresponding paper in derived publications.


