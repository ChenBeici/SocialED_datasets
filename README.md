# SocialED Datasets

This repository contains the datasets used by the [SocialED](https://github.com/RingBDStack/SocialED) Python library for social event detection tasks.

## 📁 Repository Structure

```
SocialED_dataset
├── npy_data/          # Preprocessed datasets in .npy format
├── raw_data/          # Original raw datasets
└── README.md
```

## 📊 Dataset Overview

This repository includes 14 widely-used datasets for social event detection, covering multiple languages and various event types:

|    Dataset    |       Language        |       Events        |       Texts        |    Long tail    |
| :-----------: | :---------------: | :------------------: | :------------------: | :---------------: |
| Event2012 | English | 503 | 68,841 | No |
| Event2018 | French | 257 | 64,516 | No |
| Arabic_Twitter | Arabic | 7 | 9,070 | No |
| MAVEN | English | 164 | 10,242 | No |
| CrisisLexT26 | English | 26 | 27,933 | No |
| CrisisLexT6 | English | 6 | 60,082 | No |
| CrisisMMD | English | 7 | 18,082 | No |
| CrisisNLP | English | 11 | 25,976 | No |
| HumAID | English | 19 | 76,484 | No |
| Mix_Data | English | 5 | 78,489 | No |
| KBP | English | 100 | 85,569 | No |
| Event2012_100 | English | 100 | 15,019 | Yes |
| Event2018_100 | French | 100 | 19,944 | Yes |
| Arabic_7 | Arabic | 7 | 3,022 | Yes |

## 📝 Dataset Descriptions

### General Event Detection Datasets

- **Event2012** [[Paper]](https://dl.acm.org/doi/10.1145/2505515.2505695)
  - 68,841 annotated English tweets
  - 503 distinct event categories
  - Collected over a continuous 29-day period
  - Rich temporal context for event analysis

- **Event2018** [[Paper]](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.763.pdf)
  - 64,516 annotated French tweets
  - 257 event categories
  - 23 consecutive days of data
  - Valuable insights into French social media patterns

- **Arabic_Twitter**
  - 9,070 annotated Arabic tweets
  - 7 major catastrophic events
  - Focus on crisis-related social media behavior

### Crisis-Related Datasets

- **CrisisLexT26**
  - 27,933 tweets covering 26 crisis events
  - Focus on emergency situations

- **CrisisLexT6**
  - 60,082 tweets documenting 6 major crises
  - Detailed public communication patterns

- **CrisisMMD**
  - 18,082 manually annotated tweets
  - 7 major natural disasters in 2017
  - Multimodal data including text and images

- **CrisisNLP**
  - 25,976 tweets spanning 11 events
  - Human-annotated data
  - Specialized crisis information analysis

- **HumAID**
  - 76,484 manually annotated tweets
  - 19 major natural disasters (2016-2019)
  - Diverse disaster types and locations

### Mixed and Specialized Datasets

- **MAVEN** [[Paper]](https://arxiv.org/abs/2004.13590)
  - 10,242 annotated texts
  - 164 event types
  - Domain-agnostic event detection

- **Mix_Data**
  - Composite dataset including:
    - ICWSM2018: 21,571 expert-labeled tweets
    - ISCRAM2013: 4,676 annotated tweets
    - ISCRAM2018: 49,804 tweets
    - BigCrisisData: 2,438 classified tweets

## 🔧 Usage

These datasets are ready to use with the [SocialED](https://github.com/RingBDStack/SocialED) library. You can find:
- Preprocessed data in `npy_data/`
- Original data in `raw_data/`

## 📚 Citation

If you use these datasets in your research, please cite both the original dataset papers and the SocialED library:

```bibtex
@misc{zhang2024socialedpythonlibrarysocial,
      title={SocialED: A Python Library for Social Event Detection}, 
      author={Kun Zhang and Xiaoyan Yu and Pu Li and Hao Peng and Philip S. Yu},
      year={2024},
      eprint={2412.13472},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2412.13472},
}
```

## 🔗 Related Links

- [SocialED GitHub Repository](https://github.com/RingBDStack/SocialED)
- [SocialED Documentation](https://socialed.readthedocs.io/)
- [PyPI Package](https://pypi.org/project/SocialED/)

## 📄 License

This dataset collection is released under the same license as the SocialED library. Please refer to individual dataset papers for their specific terms of use.

