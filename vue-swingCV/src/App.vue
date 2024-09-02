<template>
  <div class="upload-container">
    <h1>Upload Your Video</h1>
    <input type="file" @change="onFileChange" accept="video/*" />
    <button @click="uploadVideo">Upload</button>
    <div v-if="status" class="status">{{ status }}</div>
    <video v-if="processedVideo" :src="processedVideo" controls></video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      status: '',
      processedVideo: ''
    };
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
    },
    async uploadVideo() {
      if (!this.file) {
        this.status = "Please select a video file.";
        return;
      }

      const formData = new FormData();
      formData.append('video', this.file);

      try {
        const response = await fetch('http://localhost:5000/upload', {
          method: 'POST',
          body: formData,
        });
        const data = await response.json();

        if (response.ok) {
          this.status = data.message;
          this.processedVideo = `http://localhost:5000/${data.processed_video}`;
        } else {
          this.status = data.error;
        }
      } catch (error) {
        this.status = 'An error occurred during the upload.';
      }
    },
  },
};
</script>

<style>
.upload-container {
  text-align: center;
  margin-top: 50px;
}
.status {
  margin-top: 10px;
}
video {
  margin-top: 20px;
  max-width: 100%;
  height: auto;
}
</style>
