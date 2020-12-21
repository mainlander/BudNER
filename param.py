USE_PRETRAINED_EMBEDDING = True # 是否要使用 pre-trained word embedding
EMBEDDING_DIMENSION = 100 # Embedding維度
SENTENCE_MAX_LEN = 200 #設定一句的最大長度，這裡透過觀察資料，大部分都小於200個字，少數句子有到2000字的，但LSTM對於長句的效果不好，所以排除太長的句子
BATCH_SIZE = 32 # 設定每次進行梯度下降計算的資料筆數
EPOCHS = 10 # 設定訓練的總體迭代次數

LSTM_UNITS = 100 # LSTM隱藏層單元數

TAGS = ['O', 'B_Place', 'I_Place', 'B_Person', 'I_Person', 'B_Time', 'I_Time']
