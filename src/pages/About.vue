<template>
  <section class="w-full mb-8 relative">
    <div
      class="flex flex-col bg-cover min-h-[50vh] max-h-full items-center justify-center px-4 lg:px-72 mb-4 text-white"
      style="background-image: url(/assets/img/about-header.jpg)"
    >
      <h1 class="text-5xl font-semibold text-center mb-2">{{ $t('about.introduce.title') }}</h1>
      <p class="text-xl font-extrabold text-center md:text-start">
        {{ $t('about.introduce.contents.p1') }}
      </p>
      <p class="text-xl font-extrabold text-center md:text-start">
        {{ $t('about.introduce.contents.p2') }}
      </p>
      <p class="text-xl font-extrabold text-center md:text-start">
        {{ $t('about.introduce.contents.p3') }}
      </p>
      <p class="text-xl font-extrabold text-center md:text-start">
        {{ $t('about.introduce.contents.p4') }}
      </p>
    </div>
    <div
      class="mx-1 md:mx-4 sm:mt-[-4rem] p-2 bg-gray-100 shadow-lg border-solid border rounded-lg"
    >
      <h1 class="py-3 text-4xl font-semibold text-center mt-2">{{ $t('about.system.title') }}</h1>
      <div class="py-3">
        <div class="flex flex-wrap justify-between py-3 px-12 lg:px-36 text-center">
          <div
            class="flex flex-col mx-auto my-2 p-2 min-w-40 border-solid border rounded-lg shadow-md transform transition duration-300 ease-in-out hover:-translate-y-2"
          >
            <h5 class="text-xl font-extrabold">{{ $t('about.system.p1') }}</h5>
            <hr />
            <p class="text-lg font-semibold text-orange-500">AWS S3</p>
            <hr />
            <ul class="list-disc pl-6 text-start">
              <li>Vue3</li>
              <li>vue-router</li>
              <li>vee-validate</li>
              <li>vue-i18n</li>
              <li>Pinia</li>
              <li>tailwindcss</li>
            </ul>
          </div>
          <div
            class="flex flex-col mx-auto my-2 p-2 min-w-40 border-solid border rounded-lg shadow-md transform transition duration-300 ease-in-out hover:-translate-y-2"
          >
            <h5 class="text-xl font-extrabold">{{ $t('about.system.p2') }}</h5>
            <hr />
            <p class="text-lg font-semibold text-orange-500">AWS Lambda</p>
            <hr />
            <ul class="list-disc pl-6 text-start">
              <li>FastAPI</li>
              <li>Pydantic</li>
              <li>Motor</li>
              <li>Docker</li>
            </ul>
          </div>
          <div
            class="flex flex-col mx-auto my-2 p-2 min-w-40 border-solid border rounded-lg shadow-md transform transition duration-300 ease-in-out hover:-translate-y-2"
          >
            <h5 class="text-xl font-extrabold">{{ $t('about.system.p3') }}</h5>
            <hr />
            <p class="text-lg font-semibold text-green-600">MongoDB Atlas</p>
            <hr />
            <ul class="list-disc pl-6 text-start">
              <li>M0 Sandbox</li>
            </ul>
          </div>
        </div>
      </div>
      <h1 class="py-3 text-4xl font-semibold text-center mt-2">{{ $t('about.usage.title') }}</h1>
      <div class="py-3">
        <div class="flex flex-wrap flex-row text-center">
          <div class="flex-shrink px-4 py-2 max-x-full w-full sm:w-1/2 lg:w-1/3 lg:px-6">
            <div
              class="py-8 px-12 bg-gray-200 border-b border-gray-200 rounded-md transform transition duration-300 ease-in-out hover:-translate-y-2"
            >
              <svg
                class="w-10 h-10 mx-auto mb-2"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 384 512"
              >
                <path
                  d="M64 464H320c8.8 0 16-7.2 16-16V160H256c-17.7 0-32-14.3-32-32V48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM0 64C0 28.7 28.7 0 64 0H229.5c17 0 33.3 6.7 45.3 18.7l90.5 90.5c12 12 18.7 28.3 18.7 45.3V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V64zM192 272V400c0 6.5-3.9 12.3-9.9 14.8s-12.9 1.1-17.4-3.5L129.4 376H112c-8.8 0-16-7.2-16-16V312c0-8.8 7.2-16 16-16h17.4l35.3-35.3c4.6-4.6 11.5-5.9 17.4-3.5s9.9 8.3 9.9 14.8zm85.8-4c11.6 20 18.2 43.3 18.2 68s-6.6 48-18.2 68c-6.6 11.5-21.3 15.4-32.8 8.8s-15.4-21.3-8.8-32.8c7.5-12.9 11.8-27.9 11.8-44s-4.3-31.1-11.8-44c-6.6-11.5-2.7-26.2 8.8-32.8s26.2-2.7 32.8 8.8z"
                />
              </svg>
              <h3 class="text-lg font-semibold">{{ $t('about.usage.p1.title') }}</h3>
              <p class="text-gray-500">
                {{ $t('about.usage.p1.content') }}
              </p>
            </div>
          </div>
          <div class="flex-shrink px-4 py-2 max-x-full w-full sm:w-1/2 lg:w-1/3 lg:px-6">
            <div
              class="py-8 px-12 bg-gray-200 border-b border-gray-200 rounded-md transform transition duration-300 ease-in-out hover:-translate-y-2"
            >
              <svg
                class="w-10 h-10 mx-auto mb-2"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 640 512"
              >
                <path
                  d="M88.2 309.1c9.8-18.3 6.8-40.8-7.5-55.8C59.4 230.9 48 204 48 176c0-63.5 63.8-128 160-128s160 64.5 160 128s-63.8 128-160 128c-13.1 0-25.8-1.3-37.8-3.6c-10.4-2-21.2-.6-30.7 4.2c-4.1 2.1-8.3 4.1-12.6 6c-16 7.2-32.9 13.5-49.9 18c2.8-4.6 5.4-9.1 7.9-13.6c1.1-1.9 2.2-3.9 3.2-5.9zM0 176c0 41.8 17.2 80.1 45.9 110.3c-.9 1.7-1.9 3.5-2.8 5.1c-10.3 18.4-22.3 36.5-36.6 52.1c-6.6 7-8.3 17.2-4.6 25.9C5.8 378.3 14.4 384 24 384c43 0 86.5-13.3 122.7-29.7c4.8-2.2 9.6-4.5 14.2-6.8c15.1 3 30.9 4.5 47.1 4.5c114.9 0 208-78.8 208-176S322.9 0 208 0S0 78.8 0 176zM432 480c16.2 0 31.9-1.6 47.1-4.5c4.6 2.3 9.4 4.6 14.2 6.8C529.5 498.7 573 512 616 512c9.6 0 18.2-5.7 22-14.5c3.8-8.8 2-19-4.6-25.9c-14.2-15.6-26.2-33.7-36.6-52.1c-.9-1.7-1.9-3.4-2.8-5.1C622.8 384.1 640 345.8 640 304c0-94.4-87.9-171.5-198.2-175.8c4.1 15.2 6.2 31.2 6.2 47.8l0 .6c87.2 6.7 144 67.5 144 127.4c0 28-11.4 54.9-32.7 77.2c-14.3 15-17.3 37.6-7.5 55.8c1.1 2 2.2 4 3.2 5.9c2.5 4.5 5.2 9 7.9 13.6c-17-4.5-33.9-10.7-49.9-18c-4.3-1.9-8.5-3.9-12.6-6c-9.5-4.8-20.3-6.2-30.7-4.2c-12.1 2.4-24.7 3.6-37.8 3.6c-61.7 0-110-26.5-136.8-62.3c-16 5.4-32.8 9.4-50 11.8C279 439.8 350 480 432 480z"
                />
              </svg>
              <h3 class="text-lg font-semibold">{{ $t('about.usage.p2.title') }}</h3>
              <p class="text-gray-500">
                {{ $t('about.usage.p2.content') }}
              </p>
            </div>
          </div>
          <div class="flex-shrink px-4 py-2 max-x-full w-full sm:w-1/2 lg:w-1/3 lg:px-6">
            <div
              class="py-8 px-12 bg-gray-200 border-b border-gray-200 rounded-md transform transition duration-300 ease-in-out hover:-translate-y-2"
            >
              <svg
                class="w-10 h-10 mx-auto mb-2"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 384 512"
              >
                <path
                  d="M73 39c-14.8-9.1-33.4-9.4-48.5-.9S0 62.6 0 80V432c0 17.4 9.4 33.4 24.5 41.9s33.7 8.1 48.5-.9L361 297c14.3-8.7 23-24.2 23-41s-8.7-32.2-23-41L73 39z"
                />
              </svg>
              <h3 class="text-lg font-semibold">{{ $t('about.usage.p3.title') }}</h3>
              <p class="text-gray-500">
                {{ $t('about.usage.p3.content') }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
