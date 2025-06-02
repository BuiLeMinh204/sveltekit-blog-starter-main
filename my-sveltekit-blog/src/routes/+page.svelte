<script>
	import { siteTitle } from '$lib/config';
</script>

<svelte:head>
	<title>{siteTitle}</title>
</svelte:head>

<main class="container">
	<h1>📬 Gửi email nền với Celery + Flask</h1>
	<p>
		Dự án minh họa một ứng dụng phân tán gửi email nền bằng cách sử dụng:
	</p>
	<ul>
		<li>✅ Flask làm backend API</li>
		<li>✅ Celery xử lý tác vụ nền</li>
		<li>✅ Redis làm hàng đợi trung gian</li>
		<li>✅ SvelteKit làm frontend</li>
	</ul>
	<p>
		Bạn có thể bắt đầu gửi email tại <a href="/email">trang gửi email</a>.
	</p>
</main>

<style>
	main.container {
		max-width: 600px;
		margin: 0 auto;
		padding: 2rem;
		font-family: sans-serif;
	}
	h1 {
		font-size: 1.8rem;
		margin-bottom: 1rem;
	}
	ul {
		margin: 1rem 0;
	}
</style>
