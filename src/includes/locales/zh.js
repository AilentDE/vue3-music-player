export default {
  header: {
    about: '關於本站',
    manage: '管理曲目',
    login: '登入',
    logout: '登出'
  },
  home: {
    listen: '聽上好聽的音樂!',
    introduce:
      '歡迎來到我們的免費音樂播放平台！輕鬆上傳和播放你喜愛的歌曲。不論您是音樂家還是音樂愛好者，隨時隨地都能輕鬆享受音樂。立即免費試用我們的DEMO版本！',
    songs: '曲目'
  },
  song: {
    commentCount: '目前沒有評論 | {count} 則評論 | {count} 則評論'
  },
  auth: {
    title: '登入帳號',
    login: {
      title: '登入',
      email: 'Email',
      password: '密碼'
    },
    register: {
      title: '註冊',
      name: '名稱',
      email: 'Email',
      age: '年齡',
      password: '密碼',
      confirmPassword: '確認密碼',
      country: '國家/地區',
      accept: '我同意本站的 {0}',
      tos: '使用條款'
    }
  },
  manage: {
    upload: '上傳',
    uploadZone: '拖移檔案到這裡上傳(僅接受mp3類型)',
    mySongs: '我的曲目',
    songItem: {
      title: '標題',
      genre: '自訂類型(暫不開放)'
    }
  },
  about: {
    introduce: {
      title: '關於本站',
      contents: {
        p1: '本站是以本人技術實作的小型網站，你可以在這裡自由創建帳號、上傳音樂與播放音樂。',
        p2: '目前播放上還有些問題，以後有機會我會再來修正。(目前我得去寫別的東西了 :D)',
        p3: '由於沒有太多的伺服器資源所以運作上可能會稍微有點慢，並且有一些使用限制我會列在下面。',
        p4: '請自由的使用吧~'
      }
    },
    system: {
      title: '系統技術規格',
      p1: '前端',
      p2: '後端',
      p3: '資料庫'
    },
    usage: {
      title: '使用限制',
      p1: {
        title: '上傳檔案',
        content: '上傳檔案只能是10MB以下的mp3類型，並且會於7日後自動刪除。'
      },
      p2: {
        title: '評論',
        content: '所有留言發送後不允許編輯，並且會於7日後自動刪除。'
      },
      p3: {
        title: '播放器',
        content: '太長或太短的音樂會造成無法控制播放的問題，目前30秒左右的音樂會是最穩定的。'
      }
    }
  }
}
