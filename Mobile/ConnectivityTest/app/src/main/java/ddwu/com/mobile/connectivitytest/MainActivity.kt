package ddwu.com.mobile.connectivitytest

import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import ddwu.com.mobile.connectivitytest.databinding.ActivityMainBinding
import ddwu.com.mobile.connectivitytest.network.NetworkUtil
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    lateinit var binding: ActivityMainBinding
    lateinit var networkUtil : NetworkUtil

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        networkUtil = NetworkUtil(this)

        // 연결 정보 확인
        binding.btnConnInfo.setOnClickListener {
            networkUtil.checkNetworkStatus()        // 네트워크 연결 확인
        }

        // GET 요청 - 영화진흥위원회 API 사용 실습 시 추가 기능 구현
        binding.btnDown.setOnClickListener {
            val address = resources.getString(R.string.cs_url)   // 접속 주소

            CoroutineScope(Dispatchers.Main).launch {   // UI Thread 에서 실행
                val resultString = withContext(Dispatchers.IO) {    // IO Thread 에서 수행
                    networkUtil.downloadText(address) //이 문장을 수행할 때만 잠깐 Context를 바꿔줌. IO thread에서 수행하고 .. 결과를
                                                    //얻어온 다음 결과를 다른 곳에서 사용
                }
                Log.d("MainActivity", resultString ?: "No data")
                binding.tvDisplay.setText(resultString) // UI Thread 의 요소에 결과 출력
            }
        }

        // 이미지 다운로드
        binding.btnImg.setOnClickListener {
            val address = resources.getString(R.string.image_url)    // 접속 주소

            CoroutineScope(Dispatchers.Main).launch {   // UI Thread 에서 실행
                val bitmap = withContext(Dispatchers.IO) {    // IO Thread 에서 수행
                    networkUtil.downloadImage(address) //이 문장을 수행할 때만 잠깐 Context를 바꿔줌. IO thread에서 수행하고 .. 결과를
                    //얻어온 다음 결과를 다른 곳에서 사용
                }
                //Log.d("MainActivity", resultBitmap ?: "No data")
                binding.ivDisplay.setImageBitmap(bitmap)
            }


        }

        // POST 요청
        binding.btnSend.setOnClickListener {
            val address = resources.getString(R.string.server_url)   // 접속 주소
            val data = binding.etData.text.toString()

            CoroutineScope(Dispatchers.Main).launch {   // UI Thread 에서 실행
                val resultString = withContext(Dispatchers.IO) {    // IO Thread 에서 수행
                    networkUtil.sendPostData(address, data) //이 문장을 수행할 때만 잠깐 Context를 바꿔줌. IO thread에서 수행하고 .. 결과를
                    //얻어온 다음 결과를 다른 곳에서 사용
                }
                Log.d("MainActivity", resultString ?: "No data")
                binding.tvDisplay.setText(resultString) // UI Thread 의 요소에 결과 출력
            }
        }

    }

    override fun onPause() {
        super.onPause()
        networkUtil.stopCheckNetworkStatus()
    }
}

