<script>
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { currentPage, isMenuOpen } from '$lib/assets/js/store.js';
	import { navItems, siteTitle, siteURL } from '$lib/config.js';
	import { preloadCode } from '$app/navigation';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';

	export let data;
</script>

<svelte:head>
	<title>{siteTitle} — Send Email</title>
	<meta name="description" content="SvelteKit frontend for sending background emails using Flask + Celery" />
	<link rel="stylesheet" href="/css/root.css" />
	<link rel="stylesheet" href="/css/layout.css" />
	<link rel="stylesheet" href="/css/forms.css" />
	<link rel="alternate" type="application/rss+xml" title={siteTitle} href="http://{siteURL}/api/rss.xml" />
</svelte:head>

<div class="layout" class:open={$isMenuOpen}>
	<Header />
	{#key data.path}
		<main id="main" tabindex="-1" in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
			<slot />
		</main>
	{/key}
	<Footer />
</div>

<script>
	// Cập nhật trang hiện tại trong store
	$currentPage = data.path;

	onMount(() => {
		const navRoutes = navItems.map(item => item.route);
		preloadCode(...navRoutes);
	});
</script>

<style>
	main {
		padding: 2rem 1rem;
		min-height: 70vh;
		background-color: #f5f7fa;
	}
</style>
