import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 图片文件名列表
images = ['shanghaitech.png', 'iteration0.jpg', 'iteration50.jpg', 'iteration83.jpg', 'iteration166.jpg', 'iteration249.jpg']

# 创建一个新的figure
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# 在subplot中显示每个图像
for i, ax in enumerate(axs.flat):
    img = mpimg.imread(images[i])
    ax.imshow(img)
    ax.set_title(images[i])
    ax.axis('off')

# 调整布局并显示图像
plt.tight_layout()
plt.show()