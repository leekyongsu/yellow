<html lang="ko"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>자기소개 슬라이드</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&amp;display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
            margin: 0;
            padding: 0;
            overflow: scroll;
        }
        .slide-container {
            width: 1280px;
            min-height: 720px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
            position: relative;
        }
        .profile-circle {
            width: 180px;
            height: 180px;
            background-color: #3182ce;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 72px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .wave-decoration {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 150px;
            background: url('https://i.imgur.com/kHUVMYr.png') bottom center repeat-x;
            background-size: 1280px auto;
            opacity: 0.7;
        }
    </style>
<style>
    .genspark-badge-button {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #333;
      color: white;
      border: none;
      border-radius: 4px;
      padding: 8px 12px;
      font-size: 12px;
      cursor: pointer;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    
    .genspark-modal {
      display: none;
      position: fixed;
      bottom: 80px;
      right: 20px;
      z-index: 10000;
      justify-content: end;
    }
    
    .genspark-modal-content {
      background-color: white;
      border-radius: 8px;
      max-width: 450px;
      width: 100%;
      box-sizing: border-box;
      padding: 20px;
      position: relative;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      font-size: 14px;
    }
    @media (max-width: 768px) {
      .genspark-modal-content {
        max-width: 90%;
      }
    }
    
    .genspark-close {
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 20px;
      cursor: pointer;
      background: none;
      border: none;
    }
    
    .genspark-title {
      margin-bottom: 8px;
      font-weight: normal;
      display: inline;
      font-size: 14px;
    }
    
    .genspark-report {
      color: #909499;
      text-decoration: underline;
      cursor: pointer;
      margin-bottom: 14px;
      display: inline;
    }
    
    .genspark-info {
      margin: 25px 0;
      color: #333;
      font-size: 14px;
    }
    
    .genspark-buttons {
      display: flex;
      gap: 10px;
    }
    
    .genspark-remove-btn {
      background-color: #f5f5f5;
      border: 1px solid #ddd;
      color: #333;
      padding: 4px 14px;
      border-radius: 8px;
      cursor: pointer;
      flex: 1;
      font-size: 14px;
      box-sizing: border-box;
    }
    
    .genspark-go-btn {
      background-color: #222;
      border: none;
      color: white;
      padding: 4px 14px;
      border-radius: 8px;
      cursor: pointer;
      flex: 1;
      font-size: 14px;
      box-sizing: border-box;
    }
  </style><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script></head>
<body>
    <div class="slide-container flex flex-col items-center justify-center">
        <!-- 왼쪽 상단 장식 -->
        <div class="absolute top-0 left-0 p-8">
            <div class="w-32 h-2 bg-blue-500 rounded-full mb-2"></div>
            <div class="w-24 h-2 bg-blue-400 rounded-full mb-2"></div>
            <div class="w-16 h-2 bg-blue-300 rounded-full"></div>
        </div>
        
        <!-- 오른쪽 하단 장식 -->
        <div class="absolute bottom-0 right-0 p-8">
            <div class="w-16 h-2 bg-blue-300 rounded-full mb-2"></div>
            <div class="w-24 h-2 bg-blue-400 rounded-full mb-2"></div>
            <div class="w-32 h-2 bg-blue-500 rounded-full"></div>
        </div>
        
        <!-- 메인 콘텐츠 -->
        <div class="text-center px-20 z-10">
            <div class="profile-circle mx-auto mb-8">
                <i class="far fa-user"></i>
            </div>
            
            <h1 class="text-6xl font-bold text-gray-800 mb-6">건양대학교 안보대학원 재난안전소방학과 👋</h1>
            
            <p class="text-2xl text-gray-600 mb-8 leading-relaxed">안녕하세요, [25609506 이경수]입니다.
함께 공부하게 되어 반갑습니다.</p>
            
            <div class="mt-10 flex justify-center space-x-8">
                <div class="flex items-center">
                    <i class="fas fa-envelope text-blue-500 text-xl mr-2"></i>
                    <span class="text-gray-600">[giss3@dcc.mil.kr]</span>
                </div>
                <div class="flex items-center">
                    <i class="fas fa-phone-alt text-blue-500 text-xl mr-2"></i>
                    <span class="text-gray-600">[010-5079-2354]</span>
                </div>
            </div>
        </div>
        
        <!-- 물결 모양 하단 장식 -->
        
    </div>

 
    
        
        </body></html>
<html lang="ko"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>자기소개 슬라이드</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&amp;display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Noto Sans KR', sans-serif;
            margin: 0;
            padding: 0;
            overflow: scroll;
        }
        .slide-container {
            width: 1280px;
            min-height: 720px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
            position: relative;
        }
        .section-title {
            position: relative;
            display: inline-block;
            margin-bottom: 1.5rem;
        }
        .section-title:after {
            content: '';
            position: absolute;
            left: 0;
            bottom: -8px;
            height: 3px;
            width: 60%;
            background-color: #3182ce;
        }
        .skill-bar {
            height: 10px;
            background: #e2e8f0;
            border-radius: 5px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        .skill-fill {
            height: 100%;
            background: #3182ce;
            border-radius: 5px;
        }
        .profile-item {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .profile-icon {
            width: 36px;
            height: 36px;
            background-color: #3182ce;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            margin-right: 1rem;
        }
        .wave-decoration {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 150px;
            background: url('https://i.imgur.com/kHUVMYr.png') bottom center repeat-x;
            background-size: 1280px auto;
            opacity: 0.7;
        }
    </style>
<style>
    .genspark-badge-button {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #333;
      color: white;
      border: none;
      border-radius: 4px;
      padding: 8px 12px;
      font-size: 12px;
      cursor: pointer;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    
    .genspark-modal {
      display: none;
      position: fixed;
      bottom: 80px;
      right: 20px;
      z-index: 10000;
      justify-content: end;
    }
    
    .genspark-modal-content {
      background-color: white;
      border-radius: 8px;
      max-width: 450px;
      width: 100%;
      box-sizing: border-box;
      padding: 20px;
      position: relative;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      font-size: 14px;
    }
    @media (max-width: 768px) {
      .genspark-modal-content {
        max-width: 90%;
      }
    }
    
    .genspark-close {
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 20px;
      cursor: pointer;
      background: none;
      border: none;
    }
    
    .genspark-title {
      margin-bottom: 8px;
      font-weight: normal;
      display: inline;
      font-size: 14px;
    }
    
    .genspark-report {
      color: #909499;
      text-decoration: underline;
      cursor: pointer;
      margin-bottom: 14px;
      display: inline;
    }
    
    .genspark-info {
      margin: 25px 0;
      color: #333;
      font-size: 14px;
    }
    
    .genspark-buttons {
      display: flex;
      gap: 10px;
    }
    
    .genspark-remove-btn {
      background-color: #f5f5f5;
      border: 1px solid #ddd;
      color: #333;
      padding: 4px 14px;
      border-radius: 8px;
      cursor: pointer;
      flex: 1;
      font-size: 14px;
      box-sizing: border-box;
    }
    
    .genspark-go-btn {
      background-color: #222;
      border: none;
      color: white;
      padding: 4px 14px;
      border-radius: 8px;
      cursor: pointer;
      flex: 1;
      font-size: 14px;
      box-sizing: border-box;
    }
  </style><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script><script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script></head>
<body>
    <div class="slide-container flex flex-col">
        <!-- 왼쪽 상단 장식 -->
        <div class="absolute top-0 left-0 p-8">
            <div class="w-32 h-2 bg-blue-500 rounded-full mb-2"></div>
            <div class="w-24 h-2 bg-blue-400 rounded-full mb-2"></div>
            <div class="w-16 h-2 bg-blue-300 rounded-full"></div>
        </div>
        
        <!-- 오른쪽 하단 장식 -->
        <div class="absolute bottom-0 right-0 p-8 z-10">
            <div class="w-16 h-2 bg-blue-300 rounded-full mb-2"></div>
            <div class="w-24 h-2 bg-blue-400 rounded-full mb-2"></div>
            <div class="w-32 h-2 bg-blue-500 rounded-full"></div>
        </div>
        
        <!-- 헤더 -->
        <div class="w-full bg-white bg-opacity-50 p-6 mb-8 shadow-md">
            <h1 class="text-3xl font-bold text-gray-800 text-center">프로필 및 역량 소개</h1>
        </div>
        
        <!-- 메인 콘텐츠 -->
        <div class="flex px-12 pb-12 z-10">
            <!-- 왼쪽 열: 프로필 정보 -->
            <div class="w-1/2 pr-8">
                <h2 class="section-title text-2xl font-bold text-gray-700">개인 정보</h2>
                
                <div class="bg-white bg-opacity-70 rounded-lg p-6 shadow-md">
                    <div class="flex items-center mb-6">
                        <div class="w-20 h-20 bg-blue-500 rounded-full flex items-center justify-center text-white text-4xl mr-4">
                            <i class="far fa-user"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-semibold text-gray-800">[이경수]</h3>
                            <p class="text-gray-600">[국군방첩사령부 / 방첩팀장] </p>
                        </div>
                    </div>
                    
                    <div class="space-y-4">
                        <div class="profile-item">
                            <div class="profile-icon">
                                <i class="fas fa-graduation-cap"></i>
                            </div>
                            <div>
                                <p class="text-sm text-gray-500">학력</p>
                                <p class="text-gray-700">[중산외고 일본어과 졸업 / 서울사이버대 법무행정학과 졸업] </p>
                            </div>
                        </div>
                        
                        <div class="profile-item">
                            <div class="profile-icon">
                                <i class="fas fa-envelope"></i>
                            </div>
                            <div>
                                <p class="text-sm text-gray-500">이메일</p>
                                <p class="text-gray-700">[giss3@dcc.mil.kr] </p>
                            </div>
                        </div>
                        
                        <div class="profile-item">
                            <div class="profile-icon">
                                <i class="fas fa-phone-alt"></i>
                            </div>
                            <div>
                                <p class="text-sm text-gray-500">연락처</p>
                                <p class="text-gray-700">[010-5079-2354] </p>
                            </div>
                        </div>
                        
                        <div class="profile-item">
                            <div class="profile-icon">
                                <i class="fas fa-briefcase"></i>
                            </div>
                            <div>
                                <p class="text-sm text-gray-500">경력사항</p>
                                <p class="text-gray-700">['99년 입대 / '00년 하사 임관 / '23년 준위 임관] </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 오른쪽 열: 역량 및 강점 -->
            <div class="w-1/2 pl-8">
                <h2 class="section-title text-2xl font-bold text-gray-700">근무 경력 </h2>
                
                <div class="bg-white bg-opacity-70 rounded-lg p-6 shadow-md mb-6">
                    <div class="mb-4">
                        <div class="flex justify-between mb-1">
                            <span class="text-gray-700 font-medium">[역량 1]</span>
                            <span class="text-blue-500 font-medium">90%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" style="width: 90%"></div>
                        </div>
                    </div>
                    
                    <div class="mb-4">
                        <div class="flex justify-between mb-1">
                            <span class="text-gray-700 font-medium">[역량 2]</span>
                            <span class="text-blue-500 font-medium">85%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" style="width: 85%"></div>
                        </div>
                    </div>
                    
                    <div class="mb-4">
                        <div class="flex justify-between mb-1">
                            <span class="text-gray-700 font-medium">[역량 3]</span>
                            <span class="text-blue-500 font-medium">75%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" style="width: 75%"></div>
                        </div>
                    </div>
                </div>
                
                <h2 class="section-title text-2xl font-bold text-gray-700">강점 및 특징</h2>
                
                <div class="bg-white bg-opacity-70 rounded-lg p-6 shadow-md">
                    <div class="flex items-center mb-4">
                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-blue-500 mr-3">
                            <i class="fas fa-check"></i>
                        </div>
                        <p class="text-gray-700">[강점 1]</p>
                    </div>
                    
                    <div class="flex items-center mb-4">
                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-blue-500 mr-3">
                            <i class="fas fa-check"></i>
                        </div>
                        <p class="text-gray-700">[강점 2]</p>
                    </div>
                    
                    <div class="flex items-center">
                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center text-blue-500 mr-3">
                            <i class="fas fa-check"></i>
                        </div>
                        <p class="text-gray-700">[강점 3]</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 물결 모양 하단 장식 -->
        
    </div>


    
    
        
        </body></html>
