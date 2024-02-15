export default {
  header: {
    about: 'About',
    manage: 'Manage',
    login: 'Login',
    logout: 'Logout'
  },
  home: {
    listen: 'Listen to Great Music!',
    introduce:
      "Welcome to our free music streaming platform! Upload and play your favorite tracks hassle-free. Whether you're a musician or a music lover, enjoy seamless listening anytime, anywhere. Try our demo for free today!",
    songs: 'Songs'
  },
  song: {
    commentCount: 'No comment | 1 comment | {count} comments'
  },
  auth: {
    title: 'Your Account',
    login: {
      title: 'Login',
      email: 'Email',
      password: 'Password'
    },
    register: {
      title: 'Register',
      name: 'Name',
      email: 'Email',
      age: 'Age',
      password: 'Password',
      confirmPassword: 'Confirm Password',
      country: 'Country',
      accept: "I accept Music's {0}",
      tos: 'Terms of Service'
    }
  },
  manage: {
    upload: 'Upload',
    uploadZone: 'Drop your files here (only accept .mp3 file)',
    mySongs: 'My Songs',
    songItem: {
      title: 'Song Title',
      genre: 'Genre'
    }
  },
  about: {
    introduce: {
      title: 'About This Site',
      contents: {
        p1: 'This site is a small-scale website created by myself. Here, you can freely create an account, upload music, and play music.',
        p2: 'Currently, there are some issues with the playback, which I will fix when I have the chance. (I have to go write something else for now :D)',
        p3: 'Due to limited server resources, the operation may be a bit slow, and there are some usage restrictions, which I will list below.',
        p4: 'Feel free to use it!'
      }
    },
    system: {
      title: 'System Specifications',
      p1: 'Frontend',
      p2: 'Backend',
      p3: 'Database'
    },
    usage: {
      title: 'Usage limit',
      p1: {
        title: 'Upload file',
        content:
          'The uploaded files must be in MP3 format and are limited to 10MB or less. They will be automatically deleted after 7 days.'
      },
      p2: {
        title: 'Comments',
        content:
          'All messages sent cannot be edited and will be automatically deleted after 7 days.'
      },
      p3: {
        title: 'Player',
        content:
          'The problem of uncontrollable playback may arise with music files that are either too long or too short. Currently, music files around 30 seconds in duration are the most stable.'
      }
    }
  }
}
