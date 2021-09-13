"""
这个python包试图处理很大的图像，比如 fMOST 鼠脑图像，主要想法如下：
1. 首先训练一个深度学习神经元分割模型，它处理 32×128×128 (z*y*x) 大小的图像块，将图像块中的神经纤维从背景中分割出来
2. 然后将这些神经元图像块拼接起来得到完整神经元图像的分割结果
3. 最后使用已有的神经元追踪算法，重建分割后的神经元

但是，由于神经元图像非常大，将其分块后，图像块非常多，在处理（分割、拼接等）过程中对存储要求极大，使得速度非常慢
因此，这个脚本考虑将很大的神经元图像先划分为适当大小的图像，然后按照之前的方式处理后，再进行合并
总之，这个脚本对超大尺寸的神经元图像处理方式为

a. 若图像大小超过 ImageSize_NoMoreThan = (256, 1024, 1024), 则将其划分为 ImageSize_PartitionTo = (192, 768, 768) 的多个图像
b. 对每一个子图像进行分块处理，每个图像块大小为 32 × 128 × 128 大小
c. 对每个图像块进行分割，然后重新拼接为子图
d. 将多个子图进行合并

其中 b,c 两步其他脚本已经实现，这个包主要实现 a, d 两步
"""