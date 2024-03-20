---------------------------------------- sd_v1-5 ----------------------------------------
| sd_v1-5 | quality_level | SSIM               | Conv-Count | Linear-Count |
| ------- | ------------- | ------------------ | ---------- | ------------ |
| sd_v1-5 | 0             | 0.8165556563837066 | 98         | 184          |
| sd_v1-5 | 1             | 0.8323949474268865 | 96         | 160          |
| sd_v1-5 | 2             | 0.8348702314076454 | 88         | 142          |
| sd_v1-5 | 3             | 0.8662256561375715 | 84         | 139          |
| sd_v1-5 | 4             | 0.8707190288604787 | 62         | 113          |
---------------------------------------- end ----------------------------------------
---------------------------------------- sdxl ----------------------------------------
| sdxl | quality_level | SSIM               | Conv-Count | Linear-Count |
| ---- | ------------- | ------------------ | ---------- | ------------ |
| sdxl | 0             | 0.9426063189586985 | 51         | 743          |
| sdxl | 1             | 0.9531199491728994 | 49         | 722          |
| sdxl | 2             | 0.9615541090957868 | 45         | 659          |
| sdxl | 3             | 0.960556455965684  | 42         | 687          |
| sdxl | 4             | 0.9626790998577764 | 34         | 500          |
---------------------------------------- end ----------------------------------------
---------------------------------------- sd_v1-5_deepcache ----------------------------------------
| sd_v1-5_deepcache | quality_level | SSIM               | Conv-Count | Linear-Count |
| ----------------- | ------------- | ------------------ | ---------- | ------------ |
| sd_v1-5_deepcache | 0             | 0.8517729834085559 | 0          | 184          |
| sd_v1-5_deepcache | 1             | 0.8469390501432797 | 0          | 160          |
| sd_v1-5_deepcache | 2             | 0.8460595799988786 | 0          | 141          |
| sd_v1-5_deepcache | 3             | 0.852704767430985  | 0          | 116          |
| sd_v1-5_deepcache | 4             | 0.8509655270067743 | 0          | 109          |
---------------------------------------- end ----------------------------------------
---------------------------------------- sdxl_deepcache ----------------------------------------
| sdxl_deepcache | quality_level | SSIM               | Conv-Count | Linear-Count |
| -------------- | ------------- | ------------------ | ---------- | ------------ |
| sdxl_deepcache | 0             | 0.8990330836320674 | 0          | 743          |
| sdxl_deepcache | 1             | 0.9007828115010863 | 0          | 722          |
| sdxl_deepcache | 2             | 0.9045531115486659 | 0          | 653          |
| sdxl_deepcache | 3             | 0.9066207210614762 | 0          | 561          |
| sdxl_deepcache | 4             | 0.9074547844675099 | 0          | 504          |
---------------------------------------- end ----------------------------------------



| sd_v1-5_deepcache | PyTorch                                                               | OneDiff                                                           | SSIM   |
| ----------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ------ |
|                   | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png)       | 0.8682 |
| quality_level: 0  | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_deepcache_0.png) | 0.8518 |
| quality_level: 1  | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_deepcache_1.png) | 0.8469 |
| quality_level: 2  | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_deepcache_2.png) | 0.8461 |
| quality_level: 3  | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_deepcache_3.png) | 0.8527 |
| quality_level: 4  | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_torch.png) | ![](https://ccssu.github.io/git_pages.io/sd_v1-5_deepcache_4.png) | 0.8510 |



| sdxl_deepcache | PyTorch  | OneDiff| SSIM | 
|---|---|---|---|
|  | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png) | 0.9061| 
| quality_level: 0 | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_deepcache_0.png) | 0.8990 |
| quality_level: 1 | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_deepcache_1.png) | 0.9008 |
| quality_level: 2 | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_deepcache_2.png) | 0.9046 |
| quality_level: 3 | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_deepcache_3.png) | 0.9066 |
| quality_level: 4 | ![](https://ccssu.github.io/git_pages.io/sdxl_torch.png)|  ![](https://ccssu.github.io/git_pages.io/sdxl_deepcache_4.png) | 0.9075 |