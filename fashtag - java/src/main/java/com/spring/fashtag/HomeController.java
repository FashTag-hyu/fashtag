package com.spring.fashtag;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.UUID;

import javax.servlet.http.HttpServletRequest;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.servlet.ModelAndView;

import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {

	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);

	/**
	 * Simply selects the home view to render by returning its name.
	 */

//	@RequestMapping(value = "/insertPhoto.do", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
//	public ModelAndView test(MultipartHttpServletRequest multiRequest) throws Exception {
//		System.out.println("여기까진 왔다");
//		
//		ModelAndView mnv = new ModelAndView();
//		
//		MultipartFile mf1 = multiRequest.getFile("imgfile");
//		
//		String uploadPath = "C://uploadimage/";
//		String originalFileExtension = mf1.getOriginalFilename().substring(mf1.getOriginalFilename().lastIndexOf("."));
//		String storedFileName = UUID.randomUUID().toString().replaceAll("-", "") + originalFileExtension;
//
//		System.out.println("storedFileName : " + storedFileName);
//		
//		if (mf1.getSize() != 0) {
//			File saveFile = new File(uploadPath + storedFileName);
//			mf1.transferTo(saveFile);
//		}
//		
//		mnv.setViewName("home");
//		mnv.addObject("img", (uploadPath + storedFileName).toString());
//		mnv.addObject("img", (storedFileName).toString());
//		return mnv;
//	}

	@RequestMapping(value = "/insertPhoto.do", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String ajaxTest(MultipartHttpServletRequest multiRequest) throws Exception {
		String str = null;

		MultipartFile mf1 = multiRequest.getFile("imgFile");
		String uploadPath = "C://Users/user/PycharmProjects/fashTag/images/";
//		String originalFileExtension = mf1.getOriginalFilename().substring(mf1.getOriginalFilename().lastIndexOf("."));
		String originalFileExtension = ".jpg";
		String storedFileName = UUID.randomUUID().toString().replaceAll("-", "") + originalFileExtension;

		ObjectMapper mapper = new ObjectMapper();

		System.out.println("storedFileName : " + storedFileName);

		if (mf1.getSize() != 0) {
			File saveFile = new File(uploadPath + storedFileName);
			mf1.transferTo(saveFile);
		}
		String imgDir = uploadPath + storedFileName;

		JSONObject json = new JSONObject();
		json.put("imgDir", imgDir);

		CloseableHttpClient client = HttpClients.createDefault();
		HttpPost httpPost = new HttpPost("http://localhost:5000/");
		httpPost.addHeader("Content-type", "application/json");
		ArrayList<String> strArr = new ArrayList<String>();
		try {
			HttpURLConnection uc = (HttpURLConnection) new URL("http://localhost:5000").openConnection();

			String headerType = uc.getContentType();  
			BufferedReader in = new BufferedReader(new InputStreamReader(uc.getInputStream(),"EUC-KR"));
//			if (headerType.toUpperCase().indexOf("EUC-KR") != -1) {  
//			    in = new BufferedReader(new InputStreamReader(uc.getInputStream(),"EUC-KR"));
//			    System.out.println("EUC-KR");
//			} 
//			else if (headerType.toUpperCase().indexOf("UTF-8") != -1){  
//			    in = new BufferedReader(new InputStreamReader(uc.getInputStream(),"UTF-8"));
//			    System.out.println("UTF-8");
//			}
			
			httpPost.setEntity(new StringEntity(json.toString()));
			System.out.println(json.toString());
			
			HttpResponse response = client.execute(httpPost);
			
			System.out.println("entityTest");
			
//			String resEntity = EntityUtils.toString(response.getEntity(), "cp949");
			byte[] buf = EntityUtils.toString(response.getEntity()).getBytes("utf-8");
			
			String resEntity = new String(buf);
			
			System.out.println("RESENTITIY : " + resEntity);
			client.close();
			
			resEntity.replaceAll("\"", "-");
			resEntity = resEntity.replaceAll("\"", "");
			resEntity = resEntity.replace("[", "");
			resEntity = resEntity.replace("]", "");
			resEntity = resEntity.replaceAll(" ", "");
			String res = decode(resEntity);
			System.out.println(res);
			for(String st : res.split(",")) {
				st.trim();
				strArr.add(st);
				System.out.println(st);
			}
			
			if(strArr.get(0).equals(strArr.get(2))) {	
				if(strArr.get(0).equals("man")) {
					strArr.add("남성미 뿜뿜");
				}
				else {
					strArr.add("여성미뿜뿜");					
				}
				strArr.remove(2);
				strArr.remove(0);
			}
			else {
				strArr.add("남녀공용");
				strArr.remove(2);
				strArr.remove(0);
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		str = mapper.writeValueAsString(strArr);

		return str;
	}
	
	@RequestMapping(value = "/confDir.do", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String confDir(String text) throws Exception {
		String str = null;

		ArrayList<String> list = new ArrayList<String>();
		for(String txt : text.split("#")) {
			txt = txt.trim();
			list.add(txt);
		}
		
		list.remove(list.size()-1);
		
		System.out.println(text);
		ObjectMapper mapper = new ObjectMapper();
		str = mapper.writeValueAsString(list);
		
		return str;
	}
	
	@RequestMapping(value = "/movePhoto.do", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	public ModelAndView moveFolder(HttpServletRequest request, MultipartHttpServletRequest multiRequest) throws Exception {
		ModelAndView mnv = new ModelAndView();
//		System.out.println("movePhoto");
//		System.out.println(request.getParameter("contents"));
//		
//		MultipartFile mf1 = multiRequest.getFile("imgFile");
//		request.getAttribute("output");
//		String uploadPath = "C://Users/user/PycharmProjects/fashTag/fashion_season/";
////		String originalFileExtension = mf1.getOriginalFilename().substring(mf1.getOriginalFilename().lastIndexOf("."));
//		String originalFileExtension = ".jpg";
//		String storedFileName = UUID.randomUUID().toString().replaceAll("-", "") + originalFileExtension;
//
//		if (!mf1.isEmpty()) {
//			File saveFile = new File(uploadPath + storedFileName);
//			mf1.transferTo(saveFile);
//		}
		
		mnv.setViewName("home");
		return mnv;
	}
	
	public static String decode(String unicode) throws Exception {
	    StringBuffer str = new StringBuffer();

	    char ch = 0;
	    for( int i= unicode.indexOf("\\u"); i > -1; i = unicode.indexOf("\\u") ){
	        ch = (char)Integer.parseInt( unicode.substring( i + 2, i + 6 ) ,16);
	        str.append( unicode.substring(0, i) );
	        str.append( String.valueOf(ch) );
	        unicode = unicode.substring(i + 6);
	    }
	    str.append( unicode );

	    return str.toString();
	}
    
}




